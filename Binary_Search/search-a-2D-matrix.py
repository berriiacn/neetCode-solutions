from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        rowLength = len(matrix[0]) - 1
        while t <= b:
            midRow = (t + b)//2
            if target > matrix[midRow][rowLength]:
                t = midRow + 1
            elif target < matrix[midRow][0]:
                b = midRow - 1
            else:
                break

        l, r = 0, len(matrix[midRow]) - 1
        while l <= r:
            midCol = (l + r)//2
            if target > matrix[midRow][midCol]:
                l = midCol + 1
            elif target < matrix[midRow][midCol]:
                r = midCol - 1
            else:
                return True

        return False