class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort(reverse=True)
        n = len(candidates)

        def dfs(pos, curr, currElm):
            if pos >= n:
                return

            if curr > target:
                return

            if curr == target:
                answer.append(currElm)
                return

            dfs(pos, curr + candidates[pos], currElm + [candidates[pos]])
            dfs(pos + 1, curr, currElm)

        dfs(0, 0, [])
        return answer
