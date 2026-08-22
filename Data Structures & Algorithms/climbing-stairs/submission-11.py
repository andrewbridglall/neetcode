class Solution:
    def climbStairs(self, n: int) -> int:
        # dp - mem optimized
        dp = [1,2,0]
        if n < 3:
            return dp[n-1]
        # dp n = dp n-1 + dp n-2
        for _ in range(3, n+1):
            dp[2] = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = dp[2]
        return dp[2]