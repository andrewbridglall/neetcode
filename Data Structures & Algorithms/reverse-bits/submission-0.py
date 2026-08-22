class Solution:
    def reverseBits(self, n: int) -> int:
        res, j = 0, 0
        for i in range(31,-1,-1):
            if n & (1 << i):
                # 1 bit found
                #add to res
                res += 2**j
            j +=1
        return res