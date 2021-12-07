class Solution:
    def minWindow(self, s: str, t: str) -> str:
        diff = len(t)
        ans = [0] * 100000
        char_frequencies = {}

        for char in t:
            if char not in char_frequencies:
                char_frequencies[char] = 0
            char_frequencies[char] += 1
        k = 0
        for i, j in enumerate(s):
            if j in char_frequencies:
                char_frequencies[j] -= 1
                diff -= char_frequencies[j] >= 0

            while diff == 0:
                ans = min(ans, s[k: i + 1], key=len)
                if s[k] in char_frequencies:
                    char_frequencies[s[k]] += 1
                    diff += char_frequencies[s[k]] > 0
                k += 1

        return '' if len(ans) == 100000 else ans
