class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = [str(x) for x in digits]
        a = ''.join(a)
        a = str(int(a) + 1)
        digits = list(a)
        digits = [int(x) for x in digits]
        return digits
