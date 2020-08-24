from typing import List

# Question
# --------------
# Remove Duplicates from Sorted Array
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# --------------
#
# Description
# --------------
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# --------------


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left: int = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1


def test1():
    solution = Solution()
    answer = [1, 1, 2]
    length = solution.removeDuplicates(answer)

    assert length == 2
    for i, num in enumerate([1, 2]):
        assert answer[i] == num


def test2():
    solution = Solution()
    answer = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = solution.removeDuplicates(answer)

    assert length == 5
    for i, num in enumerate([0, 1, 2, 3, 4]):
        assert answer[i] == num
