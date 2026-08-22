class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp soln - mem optimized
        # init dp array
        n = len(cost)
        dp = [0]*(3)
        # iterate thru cost from n-1 ... 0
        for i in range(n-1, -1, -1):
            dp[0] = cost[i] + min(dp[1], dp[2])
            dp[2] = dp[1]
            dp[1] = dp[0]
        # return min dp 0 dp 1
        return min(dp[0], dp[2])