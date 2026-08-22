class Solution:
    def climbStairs(self, n: int) -> int:
        #top down - memoization
        def mem(n,cache):
            if n <=2:
                return n
            if n in cache:
                return cache[n]
            cache[n] = mem(n-1, cache) + mem(n-2, cache)
            return cache[n]
        return mem(n, {})