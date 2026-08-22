class Solution:
    def climbStairs(self, n: int) -> int:
        # bf - count ways
        cache = {}
        def dfs(summ):
            # base case
            if summ == n:
                return 1
            if summ > n:
                return 0
            if summ in cache:
                return cache[summ]
            # recursive case
            count = 0
            count += dfs(summ+1)
            count += dfs(summ+2)
            cache[summ] = count
            return cache[summ]
        return dfs(0)
