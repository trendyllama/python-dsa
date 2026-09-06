"""
Unit tests for the custom dependency injection container.

Tests cover:
- Service registration and resolution
- Scope management (singleton, transient, request-scoped)
- Async services
- Dependency resolution
- Error handling
- Circular dependency detection
"""

import asyncio
from typing import Protocol

import pytest

from src.tutorial_app.api.dependencies import (
    AsyncServiceNotSupportedError,
    CircularDependencyError,
    ServiceContainer,
    ServiceNotRegisteredError,
    create_fastapi_dependency,
)


# Test Services
class IRepository(Protocol):
    """Test interface for dependency."""

    def get(self, item_id: int) -> str: ...


class Repository:
    """Test repository service."""

    initialized: bool = False

    def __init__(self):
        self.call_count = 0

    def get(self, item_id: int) -> str:
        self.call_count += 1
        return f"data_{item_id}"


class ServiceWithDependency:
    """Test service that depends on Repository."""

    def __init__(self, repository):
        self.repository = repository

    def process(self, item_id: int) -> str:
        return self.repository.get(item_id)


class ComplexService:
    """Test service with multiple dependencies."""

    def __init__(self, repository, other_service):
        self.repository = repository
        self.other_service = other_service


class OtherService:
    """Another test service."""

    def __init__(self):
        self.value = 42


class AsyncRepository:
    """Test async repository."""

    def __init__(self):
        self.call_count = 0

    async def get(self, item_id: int) -> str:
        await asyncio.sleep(0.001)  # Simulate async work
        self.call_count += 1
        return f"async_data_{item_id}"


class ServiceWithAsyncDependency:
    """Service that depends on async repository."""

    def __init__(self, async_repository):
        self.async_repository = async_repository

    async def process(self, item_id: int) -> str:
        return await self.async_repository.get(item_id)


# Tests
class TestServiceRegistration:
    """Test service registration patterns."""

    def test_register_and_resolve_singleton(self):
        """Test singleton registration and resolution."""
        container = ServiceContainer()
        container.register(Repository).singleton()

        repo1 = container.resolve(Repository)
        repo2 = container.resolve(Repository)

        assert repo1 is repo2, "Singleton should return same instance"

    def test_register_and_resolve_transient(self):
        """Test transient registration and resolution."""
        container = ServiceContainer()
        container.register(Repository).transient()

        repo1 = container.resolve(Repository)
        repo2 = container.resolve(Repository)

        assert repo1 is not repo2, "Transient should return different instances"

    def test_register_with_factory(self):
        """Test registration with custom factory function."""
        container = ServiceContainer()

        def create_repository():
            repo = Repository()
            repo.call_count = 100  # Custom initialization
            return repo

        container.register(Repository).singleton(create_repository)
        repo = container.resolve(Repository)

        assert repo.call_count == 100, "Factory should be called during registration"

    def test_register_with_instance(self):
        """Test registration with pre-created instance."""
        container = ServiceContainer()
        repo_instance = Repository()
        repo_instance.call_count = 999

        container.register(Repository).singleton(repo_instance)
        repo = container.resolve(Repository)

        assert repo is repo_instance, "Should return the same instance"
        assert repo.call_count == 999, "Instance should have custom state"


class TestDependencyResolution:
    """Test automatic dependency resolution."""

    def test_resolve_with_constructor_dependencies(self):
        """Test automatic resolution of constructor dependencies."""
        container = ServiceContainer()
        container.register(Repository).singleton()
        container.register(ServiceWithDependency).transient()

        service = container.resolve(ServiceWithDependency)

        assert service.repository is not None
        assert isinstance(service.repository, Repository)

    def test_resolve_complex_dependencies(self):
        """Test resolution of services with multiple dependencies."""
        container = ServiceContainer()
        container.register(Repository).singleton()
        container.register(OtherService).singleton()
        container.register(ComplexService).transient()

        service = container.resolve(ComplexService)

        assert service.repository is not None
        assert service.other_service is not None
        assert isinstance(service.repository, Repository)
        assert isinstance(service.other_service, OtherService)

    def test_resolve_with_lambda_factory(self):
        """Test resolution with lambda factory that has dependencies."""
        container = ServiceContainer()
        container.register(Repository).singleton()

        def create_service(repo):
            service = ServiceWithDependency(repo)
            return service

        container.register(ServiceWithDependency).transient(create_service)
        service = container.resolve(ServiceWithDependency)

        assert service.repository is not None


class TestScopes:
    """Test service scope management."""

    def test_singleton_caching(self):
        """Test that singletons are cached."""
        container = ServiceContainer()
        container.register(Repository).singleton()

        repo = container.resolve(Repository)
        repo.call_count = 10

        repo_again = container.resolve(Repository)
        assert repo_again.call_count == 10, "Singleton should be cached"

    def test_transient_not_cached(self):
        """Test that transient services are not cached."""
        container = ServiceContainer()
        container.register(Repository).transient()

        repo1 = container.resolve(Repository)
        repo1.call_count = 10

        repo2 = container.resolve(Repository)
        assert repo2.call_count == 0, "New transient instance should have fresh state"

    def test_clear_singletons(self):
        """Test clearing singleton cache for testing."""
        container = ServiceContainer()
        container.register(Repository).singleton()

        repo1 = container.resolve(Repository)
        repo1.call_count = 50

        container.clear_singletons()
        repo2 = container.resolve(Repository)

        assert repo2 is not repo1, "New singleton should be created"
        assert repo2.call_count == 0, "New singleton should have fresh state"


class TestAsyncSupport:
    """Test async service support."""

    @pytest.mark.asyncio
    async def test_resolve_async_service(self):
        """Test resolving async services."""
        container = ServiceContainer()
        container.register(AsyncRepository).singleton()

        repo = await container.resolve_async(AsyncRepository)
        result = await repo.get(1)

        assert result == "async_data_1"

    @pytest.mark.asyncio
    async def test_async_service_with_dependencies(self):
        """Test async service resolution with dependencies."""
        container = ServiceContainer()
        container.register(AsyncRepository).singleton()
        container.register(ServiceWithAsyncDependency).transient()

        service = await container.resolve_async(ServiceWithAsyncDependency)
        result = await service.process(42)

        assert result == "async_data_42"

    @pytest.mark.asyncio
    async def test_mixed_sync_async_dependencies(self):
        """Test resolving async with sync dependencies."""
        container = ServiceContainer()
        container.register(Repository).singleton()  # Sync
        container.register(AsyncRepository).singleton()  # Async

        async_repo = await container.resolve_async(AsyncRepository)
        sync_repo = container.resolve(Repository)

        assert sync_repo is not None
        assert async_repo is not None

    def test_resolve_async_service_sync_fails(self):
        """Test that resolving async service synchronously fails."""
        container = ServiceContainer()

        async def async_factory():
            return AsyncRepository()

        container.register(AsyncRepository).singleton(async_factory)

        with pytest.raises(AsyncServiceNotSupportedError):
            container.resolve(AsyncRepository)


class TestErrorHandling:
    """Test error handling."""

    def test_service_not_registered_error(self):
        """Test error when resolving unregistered service."""
        container = ServiceContainer()

        with pytest.raises(ServiceNotRegisteredError):
            container.resolve(Repository)

    def test_circular_dependency_detection(self):
        """Test detection of circular dependencies."""

        class ServiceA:
            def __init__(self, service_b):
                self.service_b = service_b

        class ServiceB:
            def __init__(self, service_a):
                self.service_a = service_a

        container = ServiceContainer()
        container.register(ServiceA).transient(lambda b: ServiceA(b))
        container.register(ServiceB).transient(lambda a: ServiceB(a))

        with pytest.raises(CircularDependencyError):
            container.resolve(ServiceA)

    def test_resolve_nonexistent_service_async(self):
        """Test async resolution of unregistered service."""
        container = ServiceContainer()

        with pytest.raises(ServiceNotRegisteredError):
            asyncio.run(container.resolve_async(Repository))


class TestFactories:
    """Test factory function patterns."""

    def test_factory_receives_dependencies(self):
        """Test that factory functions receive resolved dependencies."""
        container = ServiceContainer()
        container.register(Repository).singleton()

        factory_calls = []

        def factory(repo):
            factory_calls.append(repo)
            return ServiceWithDependency(repo)

        container.register(ServiceWithDependency).transient(factory)
        container.resolve(ServiceWithDependency)

        assert len(factory_calls) == 1
        assert isinstance(factory_calls[0], Repository)

    def test_factory_initialization_logic(self):
        """Test complex factory initialization."""
        container = ServiceContainer()

        def create_service():
            service = Repository()
            # Complex initialization
            service.call_count = 100
            service.initialized = True
            return service

        container.register(Repository).singleton(create_service)
        repo = container.resolve(Repository)

        assert repo.call_count == 100
        assert repo.initialized is True


class TestIntegration:
    """Integration tests."""

    def test_full_dependency_chain(self):
        """Test resolving a full dependency chain."""
        container = ServiceContainer()
        container.register(Repository).singleton()
        container.register(OtherService).singleton()
        container.register(ServiceWithDependency).transient()
        container.register(ComplexService).transient()

        service = container.resolve(ComplexService)

        assert service.repository is not None
        assert service.other_service is not None
        assert service.repository.get(1) == "data_1"

    def test_multiple_registrations_chaining(self):
        """Test chaining multiple registrations."""
        container = ServiceContainer().register(Repository).singleton()
        container.register(OtherService).singleton()
        container.register(ServiceWithDependency).transient()

        all_resolved = True
        try:
            service = container.resolve(ServiceWithDependency)
            all_resolved = service.repository is not None
        except (AttributeError, TypeError, ServiceNotRegisteredError):
            all_resolved = False

        assert all_resolved

    def test_fastapi_dependency_wrapper(self):
        """Test FastAPI dependency function wrapper."""
        container = ServiceContainer()
        container.register(Repository).singleton()

        dep_func = create_fastapi_dependency(container, Repository)
        repo = dep_func()

        assert isinstance(repo, Repository)
        assert repo is container.resolve(Repository)

    @pytest.mark.asyncio
    async def test_concurrent_async_resolution(self):
        """Test concurrent async resolution."""
        container = ServiceContainer()
        container.register(AsyncRepository).singleton()

        async def resolve_many():
            tasks = [container.resolve_async(AsyncRepository) for _ in range(10)]
            return await asyncio.gather(*tasks)

        results = await resolve_many()

        # All should be the same singleton instance
        assert all(r is results[0] for r in results)


class TestRequestScope:
    """Test request-scoped dependencies."""

    def test_request_context_isolation(self):
        """Test that request contexts are isolated."""
        container = ServiceContainer()
        container.register(Repository).request_scoped()

        ctx1 = container.get_request_context(request_id=1)
        ctx2 = container.get_request_context(request_id=2)

        assert ctx1 is not ctx2

    def test_clear_request_context(self):
        """Test clearing request contexts."""
        container = ServiceContainer()

        ctx = container.get_request_context(request_id=1)
        ctx.set(Repository, Repository())

        assert ctx.get(Repository) is not None

        container.clear_request_context(request_id=1)
        ctx_new = container.get_request_context(request_id=1)
        assert ctx_new is not ctx
