class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        x = int('-' + s.strip('-') if x < 0 else int(s))
        return x if -2 ** 31 < x < 2 ** 31 - 1 else 0
