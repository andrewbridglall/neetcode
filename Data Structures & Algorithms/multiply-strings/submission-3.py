class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # alternative soln
        # get int value of num1 num2
        n1 = 0
        order = 0
        for n in reversed(num1):
            n1 += int(n)*10**(order)
            order +=1

        n2 = 0
        order = 0
        for n in reversed(num2):
            n2 += int(n)*10**(order)
            order +=1
        
        # take product and return str of res
        return str(n1 * n2)