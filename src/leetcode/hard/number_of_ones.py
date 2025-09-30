import re


class Solution:
    @staticmethod
    def count_digit_one(n: int) -> int:
        """
        Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

        Example 1:

        Input: n = 13
        Output: 6
        Example 2:

        Input: n = 0
        Output: 0

        Examples:
        >>> Solution.count_digit_one(13)
        6
        """
        if n == 0:
            return 0

        ones = (len(re.sub(r"[^1]", "", str(i))) for i in range(1, n + 1))
        return sum(ones)

    def tests(self):
        assert self.count_digit_one(13) == 6
        assert self.count_digit_one(0) == 0


if __name__ == "__main__":
    Solution().tests()
