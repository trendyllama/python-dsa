import logging

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, declarative_base

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

engine = sa.create_engine("sqlite:///:memory:")

Base: DeclarativeBase = declarative_base()


class User(Base):  # type: ignore
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(120), unique=True, nullable=False)


with engine.begin() as conn:
    Base.metadata.create_all(conn)
    conn.execute(
        sa.insert(User),
        [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
            {"name": "Alex", "email": "alex@example.com"},
            {"name": "David", "email": "david@example.com"},
        ],
    )

    result = conn.execute(
        sa.select(User).where(User.name.like("Al%")).order_by(User.id)
    ).all()
    logger.debug("Selected users with names starting with 'Al': %s", result)

    for row in result:
        logger.info("User %s: %s, %s", row.id, row.name, row.email)

    conn.execute(sa.delete(User).where(User.name == "Bob"))

    result = conn.execute(sa.select(User).order_by(User.id)).all()
    for row in result:
        logger.info("User %s: %s, %s", row.id, row.name, row.email)
