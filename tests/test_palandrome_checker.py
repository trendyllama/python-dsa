import unittest

from src.codecademy.is_palandrome import (
    IterativePalindromeChecker,
    PalindromeChecker,
    RecursivePalindromeChecker,
    SimplePalindromeChecker,
)


class TestPalindromeChecker(unittest.TestCase):
    def setUp(self) -> None:
        self.checkers: list[type[PalindromeChecker]] = [
            IterativePalindromeChecker,
            RecursivePalindromeChecker,
            SimplePalindromeChecker,
        ]

    def test_empty_string(self) -> None:
        for checker in self.checkers:
            self.assertTrue(checker("").check())

    def test_single_character(self) -> None:
        for checker in self.checkers:
            self.assertTrue(checker("a").check())
            self.assertTrue(checker("Z").check())
            self.assertTrue(checker("1").check())
            self.assertTrue(checker("@").check())
            self.assertTrue(checker(" ").check())
            self.assertTrue(checker("\n").check())
            self.assertTrue(checker("\t").check())

    def test_even_length_palindromes(self) -> None:
        palindromes = [
            "aa",
            "abba",
            "racecar",
            "noon",
            "abba",
            "deified",
            "civic",
            "redder",
        ]

        for checker in self.checkers:
            for palindrome in palindromes:
                self.assertTrue(checker(palindrome).check())
                self.assertTrue(checker(palindrome.upper()).check())

    def test_odd_length_palindromes(self) -> None:
        palindromes = [
            "aba",
            "racecar",
            "madam",
            "level",
            "rotor",
            "refer",
            "stats",
            "tenet",
        ]

        for checker in self.checkers:
            for palindrome in palindromes:
                self.assertTrue(checker(palindrome).check())
                self.assertTrue(checker(palindrome.upper()).check())

    def test_non_palindromes(self) -> None:
        non_palindromes = [
            "abc",
            "hello",
            "world",
            "python",
            "openai",
            "chatgpt",
            "data",
            "science",
        ]

        for checker in self.checkers:
            for non_palindrome in non_palindromes:
                self.assertFalse(checker(non_palindrome).check())
                self.assertFalse(checker(non_palindrome.upper()).check())
