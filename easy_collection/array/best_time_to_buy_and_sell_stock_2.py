from typing import List

# Question
# --------------
# Best Time to Buy and Sell Stock II
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# --------------
#
# Description
# --------------
# Say you have an array prices for which the ith element is the price of a
# given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# --------------


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, max_profit = 0, 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                max_profit += prices[right] - prices[left]
            left += 1

        return max_profit


def test1():
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 7


def test2():
    solution = Solution()
    prices = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices) == 4


def test3():
    solution = Solution()
    prices = [2, 3, 6]
    assert solution.maxProfit(prices) == 4


def test4():
    solution = Solution()
    prices = [1, 3, 6, 4, 2, 10]
    assert solution.maxProfit(prices) == 13
