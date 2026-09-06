"""
Custom dependency injection container with support for:
- Multiple scopes (singleton, transient, request-scoped)
- Sync and async support
- Builder pattern API
- Factory functions and automatic constructor injection
"""

from typing import (
    Any,
    Generic,
    Protocol,
    TypeVar,
    Union,
    Optional,
    get_type_hints,
)
from collections.abc import Awaitable
from collections.abc import Callable
from abc import ABC, abstractmethod
from enum import Enum
import inspect
import asyncio
from collections import defaultdict


# T = TypeVar("T")
# ServiceFactory = Callable[..., T] | Callable[..., Any]


class ServiceScope(Enum):
    """Defines the lifecycle of a service."""

    SINGLETON = "singleton"  # Single instance for application lifetime
    TRANSIENT = "transient"  # New instance on every resolution
    REQUEST = "request"  # Single instance per request context


class ServiceDescriptor[T: Awaitable]:
    """Describes a registered service."""

    def __init__(
        self,
        service_type: type[T],
        factory: Callable[..., T] | Callable[..., Any],
        scope: ServiceScope,
        is_async: bool = False,
    ):
        self.service_type = service_type
        self.factory = factory
        self.scope = scope
        self.is_async = is_async
        self.dependencies: list[type] = self._extract_dependencies()

    def _extract_dependencies(self) -> list[type]:
        """Extract constructor dependencies from the factory."""
        try:
            sig = inspect.signature(self.factory)
            hints = get_type_hints(self.factory)
            return [
                hints.get(param.name, param.annotation)
                for param in sig.parameters.values()
                if param.annotation != inspect.Parameter.empty and param.name != "self"
            ]
        except Exception:
            return []

    def is_coroutine_factory(self) -> bool:
        """Check if factory is an async function."""
        return inspect.iscoroutinefunction(self.factory)


class IServiceProvider[T](Protocol):
    """Protocol for service resolution."""

    def resolve(self, service_type: type[T]) -> T:
        """Resolve a service synchronously."""
        ...

    async def resolve_async(self, service_type: type[T]) -> T:
        """Resolve a service asynchronously."""
        ...


class RequestContext[T]:
    """Holds request-scoped service instances."""

    def __init__(self):
        self._services: dict[type, Any] = {}

    def get(self, service_type: type[T]) -> T | None:
        """Get a cached service instance."""
        return self._services.get(service_type)

    def set(self, service_type: type[T], instance: T) -> None:
        """Cache a service instance."""
        self._services[service_type] = instance


class ServiceContainer[T: Awaitable]:
    """
    Dependency injection container with support for multiple scopes and async.

    Usage:
        container = ServiceContainer()
        container.register(DatabaseService).singleton(db_service)
        container.register(RecipeService).transient(
            lambda db: RecipeService(db),
            dependencies=[DatabaseService]
        )

        recipe_service = container.resolve(RecipeService)
    """

    def __init__(self):
        self._descriptors: dict[type, ServiceDescriptor] = {}
        self._singletons: dict[type, Any] = {}
        self._request_contexts: dict[int, RequestContext] = defaultdict(RequestContext)
        self._resolution_stack: set[type] = set()

    def register(self, service_type: type[T]) -> "ServiceRegistration[T]":
        """
        Begin registration of a service.

        Args:
            service_type: The service interface/type to register

        Returns:
            ServiceRegistration for fluent API
        """
        return ServiceRegistration(self, service_type)

    def _register_descriptor(
        self,
        service_type: type[T],
        descriptor: ServiceDescriptor,
    ) -> None:
        """Register a service descriptor."""
        self._descriptors[service_type] = descriptor

    def resolve(self, service_type: type[T]) -> T:
        """
        Resolve a service synchronously.

        Args:
            service_type: The service type to resolve

        Returns:
            An instance of the service

        Raises:
            ServiceNotRegisteredError: If service not registered
            CircularDependencyError: If circular dependency detected
        """
        if service_type not in self._descriptors:
            msg = f"Service {service_type.__name__} is not registered"
            raise ServiceNotRegisteredError(
                msg
            )

        if service_type in self._resolution_stack:
            msg = f"Circular dependency detected for {service_type.__name__}"
            raise CircularDependencyError(
                msg
            )

        descriptor = self._descriptors[service_type]

        if descriptor.is_coroutine_factory():
            msg = f"Use resolve_async for async service {service_type.__name__}"
            raise AsyncServiceNotSupportedError(
                msg
            )

        # Handle singleton scope
        if descriptor.scope == ServiceScope.SINGLETON:
            if service_type in self._singletons:
                return self._singletons[service_type]

            self._resolution_stack.add(service_type)
            try:
                instance = self._resolve_sync(descriptor)
                self._singletons[service_type] = instance
                return instance
            finally:
                self._resolution_stack.discard(service_type)

        # Handle transient and request scopes
        self._resolution_stack.add(service_type)
        try:
            return self._resolve_sync(descriptor)
        finally:
            self._resolution_stack.discard(service_type)

    async def resolve_async(self, service_type: type[T]) -> T:
        """
        Resolve a service asynchronously.

        Args:
            service_type: The service type to resolve

        Returns:
            An instance of the service

        Raises:
            ServiceNotRegisteredError: If service not registered
            CircularDependencyError: If circular dependency detected
        """
        if service_type not in self._descriptors:
            msg = f"Service {service_type.__name__} is not registered"
            raise ServiceNotRegisteredError(
                msg
            )

        if service_type in self._resolution_stack:
            msg = f"Circular dependency detected for {service_type.__name__}"
            raise CircularDependencyError(
                msg
            )

        descriptor = self._descriptors[service_type]

        # Handle singleton scope
        if descriptor.scope == ServiceScope.SINGLETON:
            if service_type in self._singletons:
                return self._singletons[service_type]

            self._resolution_stack.add(service_type)
            try:
                instance = await self._resolve_async(descriptor)
                self._singletons[service_type] = instance
                return instance
            finally:
                self._resolution_stack.discard(service_type)

        # Handle transient and request scopes
        self._resolution_stack.add(service_type)
        try:
            return await self._resolve_async(descriptor)
        finally:
            self._resolution_stack.discard(service_type)

    def _resolve_sync(self, descriptor: ServiceDescriptor[T]) -> T:
        """Resolve dependencies and call factory synchronously."""
        kwargs = {}
        for param_name, dep_type in self._get_dependencies(descriptor):
            kwargs[param_name] = self.resolve(dep_type)
        return descriptor.factory(**kwargs)

    async def _resolve_async(self, descriptor: ServiceDescriptor[T]) -> T:
        """Resolve dependencies and call factory asynchronously."""
        kwargs = {}
        for param_name, dep_type in self._get_dependencies(descriptor):
            # Check if the dependency is async
            if dep_type in self._descriptors:
                dep_descriptor = self._descriptors[dep_type]
                if dep_descriptor.is_coroutine_factory():
                    kwargs[param_name] = await self.resolve_async(dep_type)
                else:
                    kwargs[param_name] = self.resolve(dep_type)
            else:
                kwargs[param_name] = self.resolve(dep_type)

        if descriptor.is_coroutine_factory():
            return await descriptor.factory(**kwargs)
        else:
            return descriptor.factory(**kwargs)

    def _get_dependencies(
        self, descriptor: ServiceDescriptor[T]
    ) -> list[tuple[str, type]]:
        if descriptor.dependencies:
            return [
                (self._get_param_name(dep_type), dep_type)
                for dep_type in descriptor.dependencies
            ]

        parameters = inspect.signature(descriptor.factory).parameters.values()
        dependencies = []
        for parameter in parameters:
            if parameter.name == "self":
                continue
            parameter_name = parameter.name.replace("_", "").lower()
            matches = [
                service_type
                for service_type in self._descriptors
                if (
                    service_type.__name__.replace("_", "").lower().startswith(parameter_name)
                    or service_type.__name__.replace("_", "").lower().endswith(parameter_name)
                )
            ]
            if len(matches) == 1:
                dependencies.append((parameter.name, matches[0]))
        return dependencies

    def _get_param_name(self, dep_type: type) -> str:
        """Get the parameter name for a dependency."""
        return dep_type.__name__[0].lower() + dep_type.__name__[1:]

    def get_request_context(self, request_id: int = 0) -> RequestContext:
        """Get or create a request context."""
        return self._request_contexts[request_id]

    def clear_request_context(self, request_id: int = 0) -> None:
        """Clear a request context."""
        if request_id in self._request_contexts:
            del self._request_contexts[request_id]

    def clear_singletons(self) -> None:
        """Clear all singleton instances (useful for testing)."""
        self._singletons.clear()


class ServiceRegistration[T: Awaitable]:
    """Fluent builder for service registration."""

    def __init__(self, container: ServiceContainer, service_type: type[T]):
        self.container = container
        self.service_type = service_type

    def singleton(
        self,
        factory: T | Callable[[], T] | None = None,
    ) -> ServiceContainer:
        """
        Register service as a singleton.

        Args:
            factory: Callable that creates the service, or an instance

        Returns:
            The container for chaining
        """
        if factory is None:
            # Use type itself as factory (constructor)
            factory = self.service_type

        # If factory is already an instance, wrap it in a lambda
        if not callable(factory):
            instance = factory
            factory = lambda: instance  # noqa: E731

        descriptor = ServiceDescriptor(
            self.service_type,
            factory,
            ServiceScope.SINGLETON,
            is_async=inspect.iscoroutinefunction(factory),
        )
        self.container._register_descriptor(self.service_type, descriptor)
        return self.container

    def transient(
        self,
        factory: Callable[[], T] | None = None,
    ) -> ServiceContainer:
        """
        Register service as transient (new instance each time).

        Args:
            factory: Callable that creates the service

        Returns:
            The container for chaining
        """
        if factory is None:
            factory = self.service_type

        descriptor = ServiceDescriptor(
            self.service_type,
            factory,
            ServiceScope.TRANSIENT,
            is_async=inspect.iscoroutinefunction(factory),
        )
        self.container._register_descriptor(self.service_type, descriptor)
        return self.container

    def request_scoped(
        self,
        factory: Callable[[], T] | None = None,
    ) -> ServiceContainer:
        """
        Register service as request-scoped.

        Args:
            factory: Callable that creates the service

        Returns:
            The container for chaining
        """
        if factory is None:
            factory = self.service_type

        descriptor = ServiceDescriptor(
            self.service_type,
            factory,
            ServiceScope.REQUEST,
            is_async=inspect.iscoroutinefunction(factory),
        )
        self.container._register_descriptor(self.service_type, descriptor)
        return self.container


# Exception classes
class DIException(Exception):
    """Base exception for dependency injection errors."""

    pass


class ServiceNotRegisteredError(DIException):
    """Raised when attempting to resolve an unregistered service."""

    pass


class CircularDependencyError(DIException):
    """Raised when a circular dependency is detected."""

    pass


class AsyncServiceNotSupportedError(DIException):
    """Raised when trying to resolve async service synchronously."""

    pass


# FastAPI integration helper
def create_fastapi_dependency[T](
    container: ServiceContainer, service_type: type[T]
) -> Callable[[], T]:
    """
    Create a FastAPI dependency function from a container.

    Usage in FastAPI:
        container = ServiceContainer()
        container.register(MyService).singleton()

        @app.get("/")
        def my_route(service: MyService = Depends(create_fastapi_dependency(container, MyService))):
            return service.do_something()
    """

    def dependency() -> T:
        return container.resolve(service_type)

    return dependency


def create_fastapi_async_dependency[T](
    container: ServiceContainer, service_type: type[T]
) -> Callable[[], Any]:
    """Create an async FastAPI dependency function from a container."""

    async def dependency() -> T:
        return await container.resolve_async(service_type)

    return dependency
