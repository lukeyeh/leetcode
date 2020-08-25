# Question
# --------------
# Rotate Image
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/rotate-image/
# --------------
#
# Description
# --------------
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
# --------------
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = matrix[i][j]
                # top left = bottom left
                matrix[i][j] = matrix[N - 1 - j][i]
                # bottom left = bottom right
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
                # bottom right = top right
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
                # top right = top left
                matrix[j][N - 1 - i] = temp


def test1():
    solution = Solution()
    matrix = [[1, 2], [3, 4]]
    solution.rotate_once(matrix, 0)
    assert matrix == [[3, 1], [4, 2]]
