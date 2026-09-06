from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel, Field


class Environment(StrEnum):
    DEV = "DEV"
    PILOT = "PILOT"
    PROD = "PROD"


class AppContext(BaseModel):
    db_path: Path
    environment: Environment = Environment.DEV
    root_path: str = ""
    is_async: bool = Field(default=True)
