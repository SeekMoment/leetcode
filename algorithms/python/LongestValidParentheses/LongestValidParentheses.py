class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i, ch in enumerate(s):
            if ch == ')' and stack and stack[-1][1] == '(':
                idx, v = stack.pop()
                ans = max(ans, i - (stack[-1][0] if stack else -1))
            else:
                stack.append((i, ch))
        return ans
