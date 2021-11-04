class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        left = right = 0
        while right < len(nums) - 1:
            maxreach = 0
            for i in range(left, right + 1):
                maxreach = max(maxreach, nums[i] + i)

            left = right + 1
            right = maxreach
            count += 1

        return count
