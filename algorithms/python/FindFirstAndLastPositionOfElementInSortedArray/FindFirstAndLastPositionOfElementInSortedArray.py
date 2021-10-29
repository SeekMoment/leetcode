class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        start = None
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if start is None:
            return [-1, -1]

        left, right = start, len(nums) - 1
        end = None
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [start, end]
