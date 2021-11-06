class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j = 0, -1
        max_j, max_i = n - 1, n - 1
        min_j, min_i = 0, 1
        count = 1
        array = [[0 for j in range(n)] for i in range(n)]
        while True:
            while j < max_j:
                j += 1
                array[i][j] = count
                count += 1
            max_j -= 1
            while i < max_i:
                i += 1
                array[i][j] = count
                count += 1
            max_i -= 1
            while j > min_j:
                j -= 1
                array[i][j] = count
                count += 1
            min_j += 1
            while i > min_i:
                i -= 1
                array[i][j] = count
                count += 1
            min_i += 1

            if j == (n - 1) // 2 and i == n // 2:
                break

        return array
