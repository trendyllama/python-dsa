"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.


Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:


I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    """

    Examples:

    >>> Solution().roman_numeral_to_int("III")
    3
    >>> Solution().roman_numeral_to_int("IV")
    4
    >>> Solution().roman_numeral_to_int("IX")
    9
    >>> Solution().roman_numeral_to_int("LVIII")
    58
    >>> Solution().roman_numeral_to_int("MCMXCIV")
    1994
    """

    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self):
        pass

    def roman_numeral_to_int(self, numeral: str) -> int:
        if len(numeral) < 1:
            raise ValueError("undefined for string inputs less than 1 chars")

        if len(numeral) > 15:
            raise ValueError("undefined for string inputs longer than 15 chars")

        result = 0

        for idx, char in enumerate(numeral):
            try:
                if numeral[idx + 1] in ["V", "X"] and char == "I":
                    result -= self.mapping[char]
                elif numeral[idx + 1] in ["L", "C"] and char == "X":
                    result -= self.mapping[char]
                elif numeral[idx + 1] in ["D", "M"] and char == "C":
                    result -= self.mapping[char]
                else:
                    result += self.mapping[char]
            except IndexError:
                result += self.mapping[char]

        return result