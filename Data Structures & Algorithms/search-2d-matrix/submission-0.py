class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            midd = (top + bot)//2
            if target > matrix[midd][-1]:
                top = midd + 1
            elif target < matrix[midd][0]:
                bot = midd - 1
            else:
                break
        if top > bot:
            return False
        left, right = 0, cols - 1
        while left <= right:
            middle = (right + left)//2
            if target == matrix[midd][middle]:
                return True
            elif target > matrix[midd][middle]:
                left = middle + 1
            else:
                right = middle - 1
        return False
