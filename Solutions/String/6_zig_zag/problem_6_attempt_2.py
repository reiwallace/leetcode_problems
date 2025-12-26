class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [""] * numRows
        counter = 0
        increase = True
        for char in s:
            rows[counter] = rows[counter] + char
            if increase:
                counter += 1
                if counter == numRows - 1:
                    increase = False
            else:
                counter -= 1
                if counter == 0:
                    increase = True
        return "".join(rows)