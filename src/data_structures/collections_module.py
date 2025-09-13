from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class UserInterface(Protocol):
    name: str
    age: int
    is_active: bool


@dataclass
class User(UserInterface):
    name: str
    age: int
    is_active: bool
