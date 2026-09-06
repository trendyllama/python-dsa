"""
Example usage of the custom dependency injection container.

This module demonstrates how to integrate the ServiceContainer
with your existing Flask/FastAPI application.
"""

from pathlib import Path
from typing import Annotated
from dataclasses import asdict

from fastapi import FastAPI, Depends
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine

from app.dependencies import (
    ServiceContainer,
    ServiceScope,
    create_fastapi_dependency,
    create_fastapi_async_dependency,
)
from app.db import (
    create_db_engine,
    create_async_db_engine,
    AppDbService,
    AsyncAppDbService,
    RecipieData,
)
from app.main import RecipeService, AsyncRecipeService, recipie_data
from app.context import AppContext


class DatabaseModule:
    """Example: Register database services in the container."""

    @staticmethod
    def configure(container: ServiceContainer, app_context: AppContext) -> None:
        """Register all database-related services."""

        # Register database engine as singleton
        if app_context.is_async:
            container.register(AsyncEngine).singleton(
                lambda: create_async_db_engine(app_context.db_path)
            )
        else:
            container.register(sa.Engine).singleton(
                lambda: create_db_engine(app_context.db_path)
            )

        # Register recipe data
        container.register(RecipieData).singleton(recipie_data())

        # Register database service as singleton
        if app_context.is_async:
            container.register(AsyncAppDbService).singleton(
                lambda engine, data: AsyncAppDbService(engine, data)
            )
        else:
            container.register(AppDbService).singleton(
                lambda engine, data: AppDbService(engine, data)
            )


class ServiceModule:
    """Example: Register business services in the container."""

    @staticmethod
    def configure(container: ServiceContainer) -> None:
        """Register all business services."""

        # Register recipe service as transient (new instance each request)
        container.register(RecipeService).transient(lambda db: RecipeService(db))

        # Alternatively, register as singleton if you want to reuse
        # container.register(RecipeService).singleton(
        #     lambda db: RecipeService(db)
        # )


# Example 1: Manual setup with container
def create_app_with_manual_di(app_context: AppContext) -> FastAPI:
    """
    Example: Create FastAPI app with manual DI container setup.

    This approach gives you full control over service registration
    and is useful for complex applications.
    """
    app = FastAPI()

    # Create and configure container
    container = ServiceContainer()
    DatabaseModule.configure(container, app_context)
    ServiceModule.configure(container)

    # Store container in app state for access in routes
    app.state.container = container

    # Example route 1: Simple dependency
    @app.get("/recipes")
    def list_recipes(
        service: RecipeService = Depends(
            create_fastapi_dependency(container, RecipeService)
        ),
    ):
        return service.get_all_recipes()

    # Example route 2: Multiple dependencies
    @app.get("/recipe/{recipe_id}")
    def get_recipe(
        recipe_id: int,
        service: RecipeService = Depends(
            create_fastapi_dependency(container, RecipeService)
        ),
    ):
        recipe, ingredients, instructions = service.get_recipe_by_id(recipe_id)
        return {
            "recipe": dict(recipe),
            "ingredients": [asdict(ing) for ing in ingredients],
            "instructions": [asdict(inst) for inst in instructions],
        }

    return app


# Example 2: Container factory pattern
class DIFactory:
    """Factory for creating and managing the DI container."""

    _container: ServiceContainer | None = None

    @classmethod
    def get_container(cls) -> ServiceContainer:
        """Get or create the global container."""
        if cls._container is None:
            cls._container = ServiceContainer()
        return cls._container

    @classmethod
    def initialize(
        cls,
        app_context: AppContext,
    ) -> ServiceContainer:
        """Initialize the container with all services."""
        container = cls.get_container()

        # Clear singletons for testing
        container.clear_singletons()

        DatabaseModule.configure(container, app_context)
        ServiceModule.configure(container)

        return container

    @classmethod
    def reset(cls) -> None:
        """Reset the container (useful for testing)."""
        if cls._container is not None:
            cls._container.clear_singletons()
        cls._container = None


# Example 3: Using container in a route handler
def get_recipe_service(container: ServiceContainer) -> RecipeService:
    """FastAPI dependency that resolves RecipeService from container."""
    return container.resolve(RecipeService)


# Example 4: Context manager for request-scoped dependencies
class RequestDIScope:
    """Manage request-scoped dependencies."""

    def __init__(self, container: ServiceContainer, request_id: int):
        self.container = container
        self.request_id = request_id

    def __enter__(self):
        """Enter request scope."""
        return self.container.get_request_context(self.request_id)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit request scope and cleanup."""
        self.container.clear_request_context(self.request_id)


# Example 5: Custom service factory with initialization
class ConfigurableRecipeService:
    """Example service that accepts configuration."""

    def __init__(self, db: sa.Engine, cache_enabled: bool = True):
        self.db = db
        self.cache_enabled = cache_enabled
        self._cache = {} if cache_enabled else None

    def get_all_recipes(self):
        if self.cache_enabled and "recipes" in self._cache:
            return self._cache["recipes"]

        stmt = sa.select(self.db).where(True)  # Placeholder
        # In real implementation, query database
        recipes = []

        if self.cache_enabled:
            self._cache["recipes"] = recipes
        return recipes


def configure_dependent_services(
    container: ServiceContainer,
    app_context: AppContext,
) -> None:
    """Register services with dependencies already in container."""

    # First, register base services
    container.register(sa.Engine).singleton(
        lambda: create_db_engine(app_context.db_path)
    )

    # Then register services that depend on them
    # The container automatically resolves dependencies from type hints
    container.register(ConfigurableRecipeService).transient(
        lambda db: ConfigurableRecipeService(db, cache_enabled=True)
    )


# Summary of usage patterns:
# 1. Singleton: One instance for entire application lifetime
#    container.register(Service).singleton()
#
# 2. Transient: New instance every time resolved
#    container.register(Service).transient()
#
# 3. Request-scoped: One instance per request
#    container.register(Service).request_scoped()
#
# 4. Custom factory: Use lambda for complex initialization
#    container.register(Service).singleton(lambda dep: Service(dep))
#
# 5. FastAPI integration:
#    @app.get("/")
#    def route(svc = Depends(create_fastapi_dependency(container, Service))):
#        return svc.do_something()
