class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        max_length = 1
        for i in range(len(s)):
            for j in range(len(s) - 1, i + max_length - 1, -1):
                if s[i:j+1] == s[i:j+1][::-1]:
                    max_length = j - i
                    res = s[i:j+1]
                    break
        return res