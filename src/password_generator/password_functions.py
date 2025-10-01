"""
Functions to generate random usernames and passwords.

"""

import logging
import random
import secrets
import string
from typing import Protocol

logger = logging.getLogger(__name__)


class StringGenerator(Protocol):
    @staticmethod
    def generate_user_name(initials: str, n: int) -> str: ...

    @staticmethod
    def generate_password(n: int) -> str: ...


class DefaultStringGenerator(StringGenerator):
    @staticmethod
    def generate_user_name(initials: str, n: int) -> str:
        return str(initials) + "".join(random.choice(string.digits) for _ in range(n))

    @staticmethod
    def generate_password(n: int) -> str:
        return "".join(
            random.choice(string.ascii_letters + string.digits + string.punctuation)
            for _ in range(n)
        )


class SecureStringGenerator(StringGenerator):
    @staticmethod
    def generate_user_name(initials: str, n: int) -> str:
        alphabet = string.ascii_letters + string.digits
        return str(initials) + "".join(secrets.choice(alphabet) for _ in range(n))

    @staticmethod
    def generate_password(n: int) -> str:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(alphabet) for _ in range(n))


def generate_user_name(initials: str, n: int) -> str:
    """
    Example
    >>> len(generate_user_name("JD", 4)) == 6
    True
    >>> isinstance(generate_user_name("JD", 4), str)
    True
    >>> generate_user_name("JD", 4).startswith("JD")
    True
    """
    logger.debug("Generating username with initials %s and %d digits", initials, n)

    return DefaultStringGenerator.generate_user_name(initials, n)


def generate_password(n: int) -> str:
    """

    Example
    >>> len(generate_password(8)) == 8
    True
    >>> isinstance(generate_password(8), str)
    True
    >>> all(
    ...     c in string.ascii_letters + string.digits + string.punctuation
    ...     for c in generate_password(8)
    ... )
    True

    """
    logger.debug("Generating password of length %d", n)

    return DefaultStringGenerator.generate_password(n)
