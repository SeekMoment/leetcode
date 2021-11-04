class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}

        for i in nums:
            d[i] = 0

        for i in range(1, n + 1):
            if i not in d:
                return i
        return i + 1
