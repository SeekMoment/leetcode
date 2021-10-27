class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)
        ans = 0

        while a >= b:
            temp = b
            mul = 1
            while a >= temp:
                a -= temp
                temp += temp
                ans += mul
                mul += mul
        if (dividend < 0 < divisor) or (dividend > 0 > divisor):
            ans = -ans
        if ans >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        if ans <= -2 ** 31:
            return -2 ** 31
        return ans
