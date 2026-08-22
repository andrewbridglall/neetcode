class Solution:
    def hammingWeight(self, n: int) -> int:
        # init var
        count = 0
        # check if 1 in 0 bit
        # n bitshift left
        for i in range(32):
            if n & (1 << i):
                count +=1
        return count