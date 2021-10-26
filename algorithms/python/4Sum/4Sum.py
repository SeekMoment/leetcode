class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = set()
        nums.sort()
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    res = nums[a] + nums[b] + nums[c] + nums[d]
                    if res == target:
                        s.add((nums[a], nums[b], nums[c], nums[d]))
                        d -= 1
                    elif res > target:
                        d -= 1
                    else:
                        c += 1
        return [list(i) for i in s]
