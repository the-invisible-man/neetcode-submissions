class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == target:
                    return True

        return False
