class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Go through the first row jut fine.
        # then go through all the last elements of all the rows
        # when you get to the last one, go through all the elements back ward
        res = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while left < right and top < bottom:
            # First we will go across the first row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # Second, we go through the final columns
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # third, we go through the last row backwards
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # finally, we go through the first column upside down
            for i in range(bottom - 1, top - 1, - 1):
                res.append(matrix[i][left])
            left += 1
        return res
