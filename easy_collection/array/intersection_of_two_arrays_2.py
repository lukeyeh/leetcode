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
# Given two arrays, write a function to compute their intersection.
# --------------


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        intersection = []
        for num in list(set(nums1).intersection(set(nums2))):
            intersection.extend([num] * min(c2[num], c1[num]))
