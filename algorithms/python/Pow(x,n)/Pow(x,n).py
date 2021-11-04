class Solution:
    def myPow(self, x: float, n: int) -> float:
        mul = 1
        m = abs(n)
        while m:
            if m % 2:
                mul = mul * x
                m -= 1
            else:
                x = x * x
                m = m // 2

        return 1 / mul if n < 0 else mul
