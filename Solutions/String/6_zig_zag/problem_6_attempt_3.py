class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [""] * numRows
        counter = 0
        increase = False
        for char in s:
            rows[counter] = rows[counter] + char
            if counter >= numRows - 1 or counter <= 0:
                increase = not increase
            if increase:
                counter += 1
            elif not increase:
                counter -= 1
        return "".join(rows)