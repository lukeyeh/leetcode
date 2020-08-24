from typing import List

# Question
# --------------
# Rotate Array
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/rotate-array/
# --------------
#
# Description
# --------------
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# --------------


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        start = count = 0

        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


def test1():
    solution = Solution()
    nums = [1, 2, 3]
    solution.rotate(nums, 1)

    print(nums)

    for i, num in enumerate([3, 1, 2]):
        assert num == nums[i]


def test2():
    solution = Solution()
    nums = [1, 2, 3, 4]
    solution.rotate(nums, 2)

    print(nums)

    for i, num in enumerate([3, 4, 1, 2]):
        assert num == nums[i]
