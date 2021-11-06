class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxreach = 0
        for i in range(n):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + nums[i])
        return True
