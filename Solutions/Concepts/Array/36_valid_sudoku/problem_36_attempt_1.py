from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            table = defaultdict(int)
            for item in row:
                table[item] += 1
                if table[item] > 1 and item != ".":
                    return False

        # Check Columns and Rows
        for column in range(9):
            table = defaultdict(int)
            for row in range(9):
                table[board[row][column]] += 1
                if table[board[row][column]] > 1 and board[row][column] != ".":
                    return False

        # Check sub-boxes
        for col_section in range(0, 8, 3):
            for row_section in range(0, 8, 3):
                table = defaultdict(int)
                for column in range(3):
                    for row in range(3):
                        table[board[row + row_section][column + col_section]] += 1
                        if table[board[row + row_section][column + col_section]] > 1 and board[row + row_section][column + col_section] != ".":
                            return False
        return True
