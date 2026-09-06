from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession

import sqlalchemy as sa
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
        recipes = list(
            (await session.scalars(sa.select(Recipe).order_by(Recipe.id))).all()
        )
        ingredients = list((await session.scalars(sa.select(Ingredient))).all())
        instructions = list((await session.scalars(sa.select(Instruction))).all())

    await engine.dispose()

    assert [recipe.name for recipe in recipes] == [
        "Fried egg",
        "Butter toast",
        "Pancakes",
        "Grilled cheese sandwich",
        "Tomato pasta",
        "Fruit smoothie",
    ]
    assert len(ingredients) == 24
    assert len(instructions) == 30


async def test_database_initialization_is_idempotent(tmp_path: Path) -> None:
    engine = create_engine(tmp_path / "recipes.db")

    await initialize_database(engine)
    await initialize_database(engine)

    async with AsyncSession(engine) as session:
        recipe_count = await session.scalar(
            sa.select(sa.func.count()).select_from(Recipe)
        )

    await engine.dispose()

    assert recipe_count == 6


async def test_database_initialization_adds_missing_seeded_records(tmp_path: Path) -> None:
    engine = create_engine(tmp_path / "recipes.db")

    await initialize_database(engine, {1: {"name": "Fried egg", "description": "Egg fried in butter", "ingredients": ["1 Egg"], "instructions": ["Cook it"]}})

    await initialize_database(engine)

    async with AsyncSession(engine) as session:
        recipes = list(
            (await session.scalars(sa.select(Recipe).order_by(Recipe.id))).all()
        )

    await engine.dispose()

    assert [recipe.name for recipe in recipes] == [
        "Fried egg",
        "Butter toast",
        "Pancakes",
        "Grilled cheese sandwich",
        "Tomato pasta",
        "Fruit smoothie",
    ]
