"""
Given a string s, return the longest
palindromic

substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def reverse_string(input_string: str) -> str:
    """
    Examples:
    >>> reverse_string("hello") == "olleh"
    True

    >>> reverse_string("racecar") == "racecar"
    True
    >>> reverse_string("a") == "a"
    True
    >>> reverse_string("") == ""
    True
    >>> reverse_string("12321") == "12321"
    True
    """
    return input_string[::-1]


def is_palandrome(input_string: str) -> bool:
    """
    Examples:
    >>> is_palandrome("hello") == False
    True
    >>> is_palandrome("racecar") == True
    True
    >>> is_palandrome("a") == True
    True
    >>> is_palandrome("") == True
    True
    >>> is_palandrome("12321") == True
    True
    """
    return input_string == reverse_string(input_string)


def get_largest_palandrome(input_string: str) -> str:
    """
    brute force method

    Examples:
    >>> get_largest_palandrome("babad") == "bab" or get_largest_palandrome("babad") == "aba"
    True
    >>> get_largest_palandrome("cbbd") == "bb"
    True
    >>> get_largest_palandrome("a") == "a"
    True

    """

    if not input_string.isalpha() or not input_string.islower():
        raise ValueError("all characters of the input string must be letters")

    if len(input_string) < 0:
        raise ValueError("unexpected input of string with a negative length")

    if len(input_string) == 0:
        return ""

    if len(input_string) == 1:
        return input_string

    if len(input_string) > 1000:
        raise ValueError("undefined for string inputs longer than 1000 chars")

    palandromes = set()

    for idx, _ in enumerate(input_string):
        for idx2, _ in enumerate(input_string):
            if is_palandrome(input_string[idx:idx2]):
                palandromes.add(input_string[idx:idx2])

    if len(palandromes) < 1:
        return ""

    return max(palandromes, key=len)
