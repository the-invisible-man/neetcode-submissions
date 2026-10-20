class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        rowMid = len(matrix) // 2
        colMid = len(matrix[0]) // 2

        b, t = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while b <= t:
            if matrix[rowMid][0] == target:
                return True
            elif matrix[rowMid][0] < target:
                b = rowMid + 1
            else:
                t = rowMid - 1

            rowMid = (b + t) // 2

        row = matrix[rowMid]

        while l <= r:
            if matrix[rowMid][colMid] == target:
                return True
            elif matrix[rowMid][colMid] < target:
                l = colMid + 1
            else:
                r = colMid - 1

            colMid = (r + l) // 2

        return False
