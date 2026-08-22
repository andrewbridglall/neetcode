class Solution:
    def reverseBits(self, n: int) -> int:
        # init new num
        res = 0
        # iter thru bits
        for i in range(32):
            if n & (1 << i):
        # add mapped 1 bits to res
                res += 1 << (31-i)
        # return res
        return res