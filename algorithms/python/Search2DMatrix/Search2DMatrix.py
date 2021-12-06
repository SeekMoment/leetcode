class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        i, j = 0, len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid][i] == target or matrix[mid][j] == target:
                return True
            elif matrix[mid][i] < target < matrix[mid][j]:
                while i <= j:
                    m = (i + j) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        i = m + 1
                    elif matrix[mid][m] > target:
                        j = m - 1

            elif matrix[mid][i] > target:
                end = mid - 1
            elif matrix[mid][j] < target:
                start = mid + 1

        return False
