import os


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

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuration:
    def __new__(cls):
        if not hasattr(Configuration, "instance"):
            cls.instance = super().__new__(cls)

        return cls.instance

    @property
    def environment(self) -> str:
        out = os.getenv("ENVIRONMENT")

        if out is None:
            raise ValueError("ENVIRONMENT variable not set")

        return out


class ApplicationState:
    def __new__(cls):
        if not hasattr(ApplicationState, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance
