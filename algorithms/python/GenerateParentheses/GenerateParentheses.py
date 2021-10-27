class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        else:
            ans = []
            k = self.generateParenthesis(n - 1)
            for each in k:
                for i in range(1, n + 1):
                    ans.append(each[:i] + '()' + each[i:])
            return list(set(ans))
