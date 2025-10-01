import pytest

from src.codecademy.is_palandrome import (
    IterativePalindromeChecker,
    PalindromeChecker,
    RecursivePalindromeChecker,
    SimplePalindromeChecker,
)


@pytest.fixture(
    params=[
        IterativePalindromeChecker,
        RecursivePalindromeChecker,
        SimplePalindromeChecker,
    ]
)
def checker(request: pytest.FixtureRequest) -> type[PalindromeChecker]:
    return request.param


def test_empty_string(checker: type[PalindromeChecker]) -> None:
    assert checker("").check()


def test_single_character(checker: type[PalindromeChecker]) -> None:
    assert checker("a").check()
    assert checker("Z").check()
    assert checker("1").check()
    assert checker("@").check()
    assert checker(" ").check()
    assert checker("\n").check()
    assert checker("\t").check()


def test_even_length_palindromes(checker: type[PalindromeChecker]) -> None:
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

    for palindrome in palindromes:
        assert checker(palindrome).check()
        assert checker(palindrome.upper()).check()


def test_odd_length_palindromes(checker: type[PalindromeChecker]) -> None:
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

    for palindrome in palindromes:
        assert checker(palindrome).check()
        assert checker(palindrome.upper()).check()


def test_non_palindromes(checker: type[PalindromeChecker]) -> None:
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

    for non_palindrome in non_palindromes:
        assert not checker(non_palindrome).check()
        assert not checker(non_palindrome.upper()).check()
