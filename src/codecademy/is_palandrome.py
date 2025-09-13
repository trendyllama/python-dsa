""" """

from typing import Protocol


class PalindromeChecker(Protocol):

    input_string: str

    def __init__(self, input_string: str) -> None: ...

    def check(self) -> bool:
        ...


class RecursivePalindromeChecker(PalindromeChecker):

    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    def check(self) -> bool:
        """
        Example:
        >>> self.check("abcba")
        True
        >>> self.check("")
        True
        >>> self.check("abcd")
        False
        """

        input_string = self.input_string

        def inner_check(input_string: str) -> bool:
            if len(input_string) < 2:
                return True
            if input_string[0] != input_string[-1]:
                return False
            return inner_check(input_string[1:-1])


        return inner_check(input_string)

class IterativePalindromeChecker(PalindromeChecker):

    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    def check(self) -> bool:
        """
        Example:
        >>> self.check("abcba")
        True
        >>> self.check("")
        True
        >>> self.check("abcd")
        False
        """
        input_string = self.input_string

        while len(input_string) > 1:
            if input_string[0] != input_string[-1]:
                return False
            input_string = input_string[1:-1]
        return True

class SimplePalindromeChecker(PalindromeChecker):

    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    def check(self) -> bool:
        """
        Example:
        >>> self.check("abcba")
        True
        >>> self.check("")
        True
        >>> self.check("abcd")
        False
        """
        return self.input_string == self.input_string[::-1]
