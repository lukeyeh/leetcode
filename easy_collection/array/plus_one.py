# Question
# --------------
# Plus One
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/plus-one/
# --------------
#
# Description
# --------------
# Given a non-empty array of digits representing a non-negative integer,
# increment one to the integer.

# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# --------------
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 0
        while True and i > -1:
            plus_one = digits[i] + carry + (1 if i == len(digits) - 1 else 0)
            carry = 1 if plus_one > 9 else 0
            digits[i] = plus_one % 10
            i -= 1

            if carry == 0:
                break

        if carry == 1:
            digits = [1] + digits

        return digits


def test1():
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]


def test2():
    solution = Solution()
    assert solution.plusOne([1, 2, 9]) == [1, 3, 0]


def test3():
    solution = Solution()
    assert solution.plusOne([9]) == [1, 0]
