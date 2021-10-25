class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    k -= 1
                elif res > 0:
                    k -= 1
                else:
                    j += 1
        return [list(i) for i in s]
