class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def solve(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation)
                return

            for num in nums:
                if num not in permutation:
                    solve(permutation + [num])

        solve([])

        return permutations
