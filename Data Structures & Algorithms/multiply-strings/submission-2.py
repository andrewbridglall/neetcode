class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # alternative soln
        # get int value of num1 num2
        n1 = 0
        order = 0
        for i in reversed(range(len(num1))):
            n1 += int(num1[i])*10**(order)
            order +=1

        n2 = 0
        order = 0
        for i in reversed(range(len(num2))):
            n2 += int(num2[i])*10**(order)
            order +=1
        
        # take product and return str of res
        return str(n1 * n2)