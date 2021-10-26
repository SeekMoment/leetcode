class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []

        for i in s:
            if i in brackets:
                if stack == [] or stack.pop() != brackets.get(i):
                    return False
            else:
                stack.append(i)

        return stack == []
