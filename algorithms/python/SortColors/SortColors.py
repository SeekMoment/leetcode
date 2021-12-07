class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l1 = {0: 0, 1: 0, 2: 0}
        for i in nums:
            l1[i] += 1

        c1, c2, c3 = l1[0], l1[1], l1[2]

        for i in range(len(nums)):

            if c1 != 0:
                nums[i] = 0
                c1 -= 1
                continue
            elif c2 != 0:
                nums[i] = 1
                c2 -= 1
                continue
            elif c3 != 0:
                nums[i] = 2
                c3 -= 1
