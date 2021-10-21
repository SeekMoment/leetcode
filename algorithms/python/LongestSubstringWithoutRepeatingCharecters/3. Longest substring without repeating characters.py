class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        t = ''
        for i in s:
            if i not in t:
                t += i
                if len(t) >= max_sub:
                    max_sub = len(t)
            else:
                t = t[t.index(i) + 1:] + i
                if len(t) >= max_sub:
                    max_sub = len(t)
        return max_sub
