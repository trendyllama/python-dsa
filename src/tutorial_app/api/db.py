from collections.abc import AsyncIterator
from pathlib import Path

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]


class Ingredient(Base):
    __tablename__ = "ingredients"

    recipe_id: Mapped[int] = mapped_column(sa.ForeignKey("recipes.id"), primary_key=True)
    name: Mapped[str] = mapped_column(primary_key=True)


class Instruction(Base):
    __tablename__ = "instructions"

    recipe_id: Mapped[int] = mapped_column(sa.ForeignKey("recipes.id"), primary_key=True)
    step_number: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]


SEED_RECIPES = {
    1: {
        "name": "Fried egg",
        "description": "Egg fried in butter",
        "ingredients": ["1 pad of butter", "1 Egg", "A pinch of salt"],
        "instructions": [
            "Melt butter in pan over medium-low heat",
            "Crack the egg into the buttered pan",
            "Sprinkle the pinch of salt onto the cooking egg",
            "Flip egg after about a minute and a half",
            "Serve egg after about a minute and a half",
        ],
    },
    2: {
        "name": "Butter toast",
        "description": None,
        "ingredients": ["1 pad of salted butter", "1 slice of bread"],
        "instructions": [
            "Put the bread in the toaster",
            "Take the toast out of the toaster",
            "Put the pad of butter on the toasted bread",
            "After a minute spread the melted butter onto the bread",
        ],
    },
}


def create_engine(db_path: Path) -> AsyncEngine:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return create_async_engine(f"sqlite+aiosqlite:///{db_path}")


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False)


async def initialize_database(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        recipe_count = await session.scalar(sa.select(sa.func.count()).select_from(Recipe))
        if recipe_count:
            return

        for recipe_id, recipe_data in SEED_RECIPES.items():
            session.add(
                Recipe(
                    id=recipe_id,
                    name=recipe_data["name"],
                    description=recipe_data["description"],
                )
            )
            session.add_all(
                Ingredient(recipe_id=recipe_id, name=name)
                for name in recipe_data["ingredients"]
            )
            session.add_all(
                Instruction(recipe_id=recipe_id, step_number=step, text=text)
                for step, text in enumerate(recipe_data["instructions"], start=1)
            )
        await session.commit()


async def close_engine(engine: AsyncEngine) -> None:
    await engine.dispose()


async def get_session(engine: AsyncEngine) -> AsyncIterator[AsyncSession]:
    async_session = create_session_factory(engine)
    async with async_session() as session:
        yield session