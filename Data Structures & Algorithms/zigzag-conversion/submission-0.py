class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        rows = [""] * numRows
        step = 1
        current_row = 0
        for letter in s:
            rows[current_row] += letter
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            current_row += step
        return ("").join(rows)