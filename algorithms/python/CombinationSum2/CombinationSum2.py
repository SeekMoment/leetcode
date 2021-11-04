import numpy as np


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def recursive(start, comboSum, combo):
            if comboSum == target:
                answer.append(combo)

            for i in range(start, len(candidates)):
                if comboSum + candidates[i] <= target:
                    if i != start and candidates[i] == candidates[i - 1]:
                        continue
                    newCombo = combo + [candidates[i]]
                    recursive(i + 1, comboSum + candidates[i], newCombo)
            return answer

        recursive(0, 0, [])
        return answer
