""" """

import logging
from typing import Protocol

logger = logging.getLogger(__name__)


class PalindromeChecker(Protocol):
    input_string: str

    def __init__(self, input_string: str) -> None: ...

    def check(self) -> bool: ...


class RecursivePalindromeChecker(PalindromeChecker):
    def __init__(self, input_string: str) -> None:
        logger.debug(
            "Initializing RecursivePalindromeChecker with input: '%s'", input_string
        )
        self.input_string = input_string

    def check(self) -> bool:
        """
        Example:
        >>> checker = RecursivePalindromeChecker("abcba")
        >>> checker.check()
        True
        >>> checker = RecursivePalindromeChecker("")
        >>> checker.check()
        True
        >>> checker = RecursivePalindromeChecker("abcd")
        >>> checker.check()
        False
        """

        input_string = self.input_string
        logger.debug("Checking if '%s' is a palindrome", input_string)

        def inner_check(input_string: str) -> bool:
            if len(input_string) < 2:
                logger.debug("Base case reached with string: '%s'", input_string)
                return True
            if input_string[0] != input_string[-1]:
                logger.debug(
                    "Characters '%s' and '%s' do not match",
                    input_string[0],
                    input_string[-1],
                )
                return False
            return inner_check(input_string[1:-1])

        return inner_check(input_string)


class IterativePalindromeChecker(PalindromeChecker):
    def __init__(self, input_string: str) -> None:
        logger.debug(
            "Initializing IterativePalindromeChecker with input: '%s'", input_string
        )
        self.input_string = input_string

    def check(self) -> bool:
        """
        Example:
        >>> checker = IterativePalindromeChecker("abcba")
        >>> checker.check()
        True
        >>> checker = IterativePalindromeChecker("")
        >>> checker.check()
        True
        >>> checker = IterativePalindromeChecker("abcd")
        >>> checker.check()
        False
        """
        input_string = self.input_string

        while len(input_string) > 1:
            logger.debug("Comparing '%s' and '%s'", input_string[0], input_string[-1])
            if input_string[0] != input_string[-1]:
                logger.debug(
                    "Characters '%s' and '%s' do not match",
                    input_string[0],
                    input_string[-1],
                )
                return False
            input_string = input_string[1:-1]
            logger.debug("Trimmed string to '%s'", input_string)
        return True


class SimplePalindromeChecker(PalindromeChecker):
    def __init__(self, input_string: str) -> None:
        logger.debug(
            "Initializing SimplePalindromeChecker with input: '%s'", input_string
        )
        self.input_string = input_string

    def check(self) -> bool:
        """
        Example:
        >>> checker = SimplePalindromeChecker("abcba")
        >>> checker.check()
        True
        >>> checker = SimplePalindromeChecker("")
        >>> checker.check()
        True
        >>> checker = SimplePalindromeChecker("abcd")
        >>> checker.check()
        False
        """
        return self.input_string == self.input_string[::-1]
