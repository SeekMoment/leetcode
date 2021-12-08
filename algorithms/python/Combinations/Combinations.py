class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def combo(n, curr, k, pos):
            if len(curr) == k:
                ans.append(curr)
            for i in range(pos + 1, n + 1):
                combo(n, curr + [i], k, i)

        combo(n, [], k, 0)
        return ans
