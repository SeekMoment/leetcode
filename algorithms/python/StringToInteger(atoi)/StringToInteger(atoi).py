class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.strip()
        if s == '':
            return 0
        char = s[0]
        if char == '-' or char == '+':
            s = s[1:]
            if char == '-':
                sign = -1
        ans = 0
        for i in s:
            if '0' <= i <= '9':
                ans = ans * 10 + int(i)
            else:
                break
        ans = ans * sign
        if ans < -2 ** 31:
            return -2 ** 31
        elif ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return ans
