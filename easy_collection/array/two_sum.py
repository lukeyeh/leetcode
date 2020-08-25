# Question
# --------------
# Two Sum
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/two-sum/
# --------------
#
# Description
# --------------
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# --------------
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in m:
                return [m[compliment], i]
            m[num] = i

        # Not possible given the assumption that each input would have exactly
        # one solution.
        return None


def test1():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
