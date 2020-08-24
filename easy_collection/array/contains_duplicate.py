from typing import List

# Question
# --------------
# Contains Duplicate
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/contains-duplicate/
# --------------
#
# Description
# --------------
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# --------------


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        left = 0
        for right in range(1, len(nums)):
            if nums[left] == nums[right]:
                return True
            left += 1

        return False


def test1():
    solution = Solution()
    nums = [1, 2, 3, 4]
    assert not solution.containsDuplicate(nums)


def test2():
    solution = Solution()
    nums = [1, 1, 2, 3]
    assert solution.containsDuplicate(nums)


def test3():
    solution = Solution()
    nums = [1, 2, 2, 3]
    assert solution.containsDuplicate(nums)
