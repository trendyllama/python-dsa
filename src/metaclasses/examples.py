from typing import ClassVar


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

    _instances: ClassVar[dict[type, object]] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance


class VariantMeta(type):
    """
    A metaclass for creating variant classes.

    Example:
    >>> class MyVariant(metaclass=VariantMeta):
    ...     pass
    >>> variant1 = MyVariant()
    >>> variant2 = MyVariant()
    >>> variant1 is variant2
    False
    >>> variant1 == variant2
    False

    """

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        return instance


class ImmutableMeta(type):
    """
    A metaclass for creating immutable classes.

    Example:
    >>> class MyImmutable(metaclass=ImmutableMeta):
    ...     def __init__(self, value):
    ...         self.value = value
    >>> immutable1 = MyImmutable(10)
    >>> immutable2 = MyImmutable(10)
    >>> immutable1 is immutable2
    False

    """

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        return instance

    def __setattr__(cls, key, value):
        raise AttributeError("Cannot modify immutable class attributes")

    def __delattr__(cls, key):
        raise AttributeError("Cannot delete immutable class attributes")

    def __setitem__(cls, key, value):
        raise AttributeError("Cannot modify immutable class items")

    def __delitem__(cls, key):
        raise AttributeError("Cannot delete immutable class items")
