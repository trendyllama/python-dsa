import os
from typing import Self


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

    _instances: dict = {}

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

    def __init__(self):
        env_var = os.getenv("ENVIRONMENT")
        if env_var is None:
            raise ValueError("ENVIRONMENT variable not set")

        self.environment: str = env_var


class ApplicationState:
    _instances = {}

    def __new__(cls) -> Self:
        if cls not in cls._instances:
            cls.instance = super().__new__(cls)

        return cls.instance
