from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for i in range(9)] for i in range(9)]
        cols = [[False for i in range(9)] for i in range(9)]
        sub = [[False for i in range(9)] for i in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = int(board[row][col]) - 1
                    cur_sub = (row // 3) * 3 + (col // 3)
                    if rows[row][num] or cols[col][num] or sub[cur_sub][num]:
                        return False
                    rows[row][num] = cols[col][num] = sub[cur_sub][num] = True
        return True