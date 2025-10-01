import os
from typing import ClassVar, Self


class SingletonMeta(type):
    """
    A metaclass for creating singleton classes. Ensures that only one instance of the class can exist.


    Example:
    >>> class MySingleton(metaclass=SingletonMeta):
    ...     pass
    >>> instance1 = MySingleton()
    >>> instance2 = MySingleton()
    >>> instance1 is instance2
    True
    >>> instance1 == instance2
    True

    """

    _instances: ClassVar[dict] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuration(SingletonMeta):
    """
    A singleton class that holds configuration settings for the application.

    It reads the environment variable "ENVIRONMENT" to determine the configuration.
    """

    def __init__(cls):
        env_var = os.getenv("ENVIRONMENT")
        if env_var is None:
            msg = "ENVIRONMENT variable not set"
            raise ValueError(msg)

        cls.environment: str = env_var


class ApplicationState:
    _instances: ClassVar[dict] = {}

    def __new__(cls) -> Self:
        if cls not in cls._instances:
            cls.instance = super().__new__(cls)

        return cls.instance
