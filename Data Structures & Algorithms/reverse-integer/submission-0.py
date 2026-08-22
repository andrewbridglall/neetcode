class Solution:
    def reverse(self, x: int) -> int:
        # handle negs
        sign = 1
        # convert to str
        # reverse str
        strRes = "".join(reversed(str(x)))
        if strRes[-1] == "-":
            sign = -1
            intRes = -1*int(strRes[:-1])
        else:
            intRes = int(strRes)
        # convert to int
        # check int is valid
        # return 0 if invalid else ret int
        return intRes if (-1)*(2**31) < intRes <= 2**31 -1 else 0