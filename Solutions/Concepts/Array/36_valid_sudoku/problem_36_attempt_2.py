from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            table = defaultdict(int)
            for column in row:
                if column == ".": continue
                table[column] += 1
                if table[column] > 1:
                    return False

        # Check columns
        for column in range(9):
            table = defaultdict(int)
            for row in range(9):
                if board[row][column] == ".": continue
                table[board[row][column]] += 1
                if table[board[row][column]] > 1:
                    return False

        # Check sub-boxes
        for col_section in range(0, 8, 3):
            for row_section in range(0, 8, 3):
                table = defaultdict(int)
                for column in range(col_section, col_section + 3):
                    for row in range(row_section, row_section + 3):
                        if board[row][column] == ".": continue
                        table[board[row][column]] += 1
                        if table[board[row][column]] > 1:
                            return False
        return True
