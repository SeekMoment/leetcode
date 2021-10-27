class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums[::-1]:
            if nums.count(i) > 1:
                nums.remove(i)
        return len(nums)
