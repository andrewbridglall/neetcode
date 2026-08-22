class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask32 = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b != 0:
            # get carry
            carry = (a & b) << 1
            # get digit
            a = (a ^ b) & mask32
            b = carry & mask32
        # handle edge case
        return a if a <= maxInt else ~(a ^ mask32)