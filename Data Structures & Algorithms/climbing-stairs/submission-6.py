class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, nxt = 1,2
        for _ in range(3, n+1):
            tmp = prev+nxt
            prev = nxt
            nxt = tmp
        return nxt
