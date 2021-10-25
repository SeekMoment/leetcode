class Solution:
    letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def digit_generator(self, total, num):
        if not total:
            return self.letters[num]
        temp = []
        for j in total:
            for k in self.letters[num]:
                temp.append(j + k)
        return temp

    def letterCombinations(self, digits: str) -> List[str]:
        total = []
        for i in digits:
            total = self.digit_generator(total, i)
        return total
