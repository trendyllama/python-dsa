"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

"""


def binary_search(nums: list[int], target: int) -> int:
    """

    TODO: handle empty list case

    TODO: handle the copies of the original list

    Examples:
    >>> binary_search([-1, 0, 3, 5, 9, 12], 9)
    4
    >>> binary_search([-1, 0, 3, 5, 9, 12], 2)
    -1
    >>> binary_search([], 2)
    -1
    >>> binary_search([1, 2, 3, 4, 5], 3)
    2


    """

    sorted_nums = sorted(nums)

    if len(sorted_nums) == 0:
        return -1

    left = 0
    right = len(sorted_nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate middle index

        if sorted_nums[mid] == target:
            return mid  # Target found
        elif sorted_nums[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found


def binary_search_recursive(nums: list[int], target: int) -> int:
    """
    Recursive implementation of binary search.

    Examples:
    >>> binary_search_recursive([-1, 0, 3, 5, 9, 12], 9)
    4
    >>> binary_search_recursive([-1, 0, 3, 5, 9, 12], 2)
    -1
    >>> binary_search_recursive([], 2)
    -1
    >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
    2
    """

    def inner_func(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return inner_func(mid + 1, right)
        else:
            return inner_func(left, mid - 1)

    result = inner_func(0, len(nums) - 1)

    if not isinstance(result, int):
        msg = "Recursion did not return an integer index."
        raise RecursionError(msg)

    return result
