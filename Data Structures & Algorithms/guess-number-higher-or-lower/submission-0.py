# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s, e = 1, n

        while s<=e:
            num = (s+e)//2
            if guess(num) > 0:
                s = num+1
            elif guess(num) < 0:
                e = num-1
            else:
                return num
        return -1