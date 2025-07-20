

class SingletonMeta(type):
    """
    A metaclass for creating singleton classes.

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
