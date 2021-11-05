class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        x, y = 0, -1
        dx, dy = 0, 1

        ans = []

        while count < rows * cols:
            x, y = x + dx, y + dy
            ans.append(matrix[x][y])
            matrix[x][y] = None
            count += 1

            if x + dx >= rows or y + dy >= cols or matrix[x + dx][y + dy] is None:
                dx, dy = dy, -dx

        return ans
