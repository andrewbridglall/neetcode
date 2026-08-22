class Solution:
    def isHappy(self, n: int) -> bool:
        # init vars
        sumSet = set()
        # calc sum of squares in a loop
        while n != 1:
            summ = 0
            for digit in str(n):
                summ += int(digit)**2
            if summ in sumSet:
                return False
            sumSet.add(summ)
            n = summ
            print(n)
        # if sum == 1 ret true
        return True