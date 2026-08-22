class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # basic multiplication
        # reverse num1 num2 st magnitude of digits increasing
        number1, number2 = num1[::-1], num2[::-1]
        n,m = len(number1), len(number2)
        # take product of each digit of num1 and each digit of num2
        res = 0
        for i in range(n):
            for j in range(m):
                res += int(number1[i]) * 10**(i) * int(number2[j]) * 10**(j)
        return str(res)