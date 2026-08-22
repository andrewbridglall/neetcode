class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 2**32-1 #32 bit int
        max_signed = 2**31-1 #max signed 32 bit it, last bit for sign

        while a & b:
            res1 = (a ^ b) & mask
            res2 = ((a & b) << 1) & mask
            a,b = res1, res2
        # if res negative, flip sign
        res = a ^ b
        return res if res <= max_signed else ~(res ^ mask)