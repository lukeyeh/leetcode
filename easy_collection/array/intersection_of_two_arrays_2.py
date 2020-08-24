from typing import List

# Question
# --------------
# Intersection of Two Arrays II
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# --------------
#
# Description
# --------------
# Intersection of Two Arrays II
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# --------------
#
# Description
# --------------
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# --------------
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        intersection = []
        for num in list(set(nums1).intersection(set(nums2))):
            intersection.extend([num] * min(c2[num], c1[num]))

        return intersection


def test1():
    solution = Solution()
    intersect = solution.intersect([1, 2, 2, 1], [2, 2])
    # this tests for equality of elements without order.
    # see: https://stackoverflow.com/questions/31501909/
    assert frozenset(intersect) == frozenset([2, 2])


def test2():
    solution = Solution()
    intersect = solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])
    assert frozenset(intersect) == frozenset([9, 4])


def test3():
    solution = Solution()
    intersect = solution.intersect([2, 1], [1, 1])
    assert frozenset(intersect) == frozenset([1])
