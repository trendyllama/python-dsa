"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less
than O(n2) time complexity?
"""


class Solution:
    """
    represents the implementation of the solution

    also can be extened to include the faster solution
    """

    def two_sums(self, nums: list[int], target: int) -> list[int] | None:
        """

        Examples:
        >>> Solution().two_sums([2, 7, 11, 15], 9) == [0, 1]
        True
        >>> Solution().two_sums([3, 2, 4], 6) == [1, 2]
        True
        >>> Solution().two_sums([3, 3], 6) == [0, 1]
        True
        """
        if len(nums) < 2:
            raise ValueError

        if len(nums) > 104:
            raise ValueError

        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if idx1 == idx2:
                    continue

                if val1 == (target - val2):
                    return [idx1, idx2]

        return None
