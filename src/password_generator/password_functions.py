"""
Functions to generate random usernames and passwords.

"""

import secrets
import string


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

    return str(initials) + "".join([secrets.choice(string.digits) for _ in range(n)])


def generate_password(n: int) -> str:
    """

    Example
    >>> len(generate_password(8)) == 8
    True
    >>> isinstance(generate_password(8), str)
    True
    >>> all(c in string.ascii_letters + string.digits + string.punctuation for c in generate_password(8))
    True

    """
    return "".join(
        [
            secrets.choice(string.ascii_letters + string.digits + string.punctuation)
            for _ in range(n)
        ]
    )
