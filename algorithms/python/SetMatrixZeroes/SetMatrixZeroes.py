class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroLocations = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroLocations.append([i, j])

        seenRows = set()
        seenCols = set()

        for location in zeroLocations:
            row, col = location

            if row not in seenRows:
                self.zeroRow(matrix, row)
                seenRows.add(row)
            if col not in seenCols:
                self.zeroCol(matrix, col)
                seenCols.add(col)

    def zeroRow(self, matrix, row) -> None:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0

    def zeroCol(self, matrix, col) -> None:
        for row in range(len(matrix)):
            matrix[row][col] = 0
