class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, pre = nums[0], nums[0]
        for num in nums[1:]:
            if pre < 0:
                pre = 0
            pre += num
            res = max(res, pre)

        return res
