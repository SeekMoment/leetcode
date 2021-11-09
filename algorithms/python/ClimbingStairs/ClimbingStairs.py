class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1, 2):
            return n
        a = 1
        b = 2
        for i in range(n - 2):
            a, b = b, a + b
        return b
