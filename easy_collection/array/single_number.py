from typing import List

# Question
# --------------
# Single Number
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/contains-duplicate/
# --------------
#
# Description
# --------------
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# --------------


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # One-liner:
        # Time: O(n)
        # Space: O(n)
        # Counter(nums).most_common()[-1][0]
        b = 0
        for num in nums:
            b ^= num

        return b
