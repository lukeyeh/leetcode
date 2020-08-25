# Question
# --------------
# Valid Sudoku
# --------------
#
# Link
# --------------
# https://leetcode.com/problems/valid-sudoku/
# --------------
#
# Description
# --------------
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
#    without repetition.
# --------------
from collections import defaultdict
from typing import List, Tuple, DefaultDict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_index(z: int):
            ranges = [(0, 2), (3, 5), (6, 8)]
            for i, r in enumerate(ranges):
                if r[0] <= z <= r[1]:
                    return i

        def get_square(i: int, j: int) -> Tuple[int, int]:
            return (get_index(i), get_index(j))

        row_mem = defaultdict(set)
        column_mem = defaultdict(set)
        square_mem: DefaultDict[Tuple[int, int], int] = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == '.':
                    continue
                if num in row_mem[i]:
                    return False
                else:
                    row_mem[i].add(num)

                if num in column_mem[j]:
                    return False
                else:
                    column_mem[j].add(num)

                square: Tuple[int, int] = get_square(i, j)
                if num in square_mem[square]:
                    return False
                else:
                    square_mem[square].add(board[i][j])

        return True


def test1():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
