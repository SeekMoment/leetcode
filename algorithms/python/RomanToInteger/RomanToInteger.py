class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        special_cases = {'IV': 4,
                         'IX': 9,
                         'XL': 40,
                         'XC': 90,
                         'CD': 400,
                         'CM': 900}
        for case, value in special_cases.items():
            res += s.count(case) * value
            s = s.replace(case, '')

        regular_cases = {'I': 1,
                         'V': 5,
                         'X': 10,
                         'L': 50,
                         'C': 100,
                         'D': 500,
                         'M': 1000}
        for one_char in s:
            res += regular_cases[one_char]

        return res
