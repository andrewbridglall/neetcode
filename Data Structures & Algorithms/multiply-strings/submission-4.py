class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # alternative soln
        # get int value of num1 num2
        n,m = len(num1), len(num2)
        n1 = 0
        for i in reversed(range(n)):
            n1 += int(num1[i])*10**(n-1 - i)

        n2 = 0
        for i in reversed(range(m)):
            n2 += int(num2[i])*10**(m-1 - i)
                    
        # take product and return str of res
        return str(n1 * n2)