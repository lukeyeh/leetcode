# Question
# --------------
# Move Zeroes
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/move-zeroes/
# --------------
#
# Description
# --------------
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# --------------
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_index] = nums[i]
                write_index += 1

        # write_index == number of non-zero nums
        # => number of zeros == len(nums) - write_index
        num_zeroes = len(nums) - write_index
        nums[write_index:] = [0] * num_zeroes

        return nums


def test1():
    solution = Solution()
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test2():
    solution = Solution()
    assert solution.moveZeroes([0, 0, 1, 3, 12]) == [1, 3, 12, 0, 0]


def test3():
    solution = Solution()
    assert solution.moveZeroes([1, 2, 3, 4]) == [1, 2, 3, 4]


def test4():
    solution = Solution()
    assert solution.moveZeroes([]) == []


def test5():
    solution = Solution()
    assert solution.moveZeroes([0, 0, 0, 0, 1]) == [1, 0, 0, 0, 0]
