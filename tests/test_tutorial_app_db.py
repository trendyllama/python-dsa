from pathlib import Path

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from src.tutorial_app.api.db import (
    Ingredient,
    Instruction,
    Recipe,
    create_engine,
    initialize_database,
)


async def test_database_initialization_creates_seeded_records(tmp_path: Path) -> None:
    engine = create_engine(tmp_path / "recipes.db")

    await initialize_database(engine)

    async with AsyncSession(engine) as session:
        recipes = list((await session.scalars(sa.select(Recipe).order_by(Recipe.id))).all())
        ingredients = list((await session.scalars(sa.select(Ingredient))).all())
        instructions = list((await session.scalars(sa.select(Instruction))).all())

    await engine.dispose()

    assert [recipe.name for recipe in recipes] == ["Fried egg", "Butter toast"]
    assert len(ingredients) == 5
    assert len(instructions) == 9


async def test_database_initialization_is_idempotent(tmp_path: Path) -> None:
    engine = create_engine(tmp_path / "recipes.db")

    await initialize_database(engine)
    await initialize_database(engine)

    async with AsyncSession(engine) as session:
        recipe_count = await session.scalar(sa.select(sa.func.count()).select_from(Recipe))

    await engine.dispose()

    assert recipe_count == 2