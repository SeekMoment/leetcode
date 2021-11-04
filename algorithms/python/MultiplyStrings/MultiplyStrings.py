class Solution:
    def get_integer(self, num_str: str) -> int:
        num = 0
        for i in num_str:
            num = num * 10 + ord(i) - 48

        return num

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.get_integer(num1) * self.get_integer(num2))
