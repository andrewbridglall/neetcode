class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp soln
        # init dp array
        n = len(cost)
        dp = [0]*(n+2)
        # iterate thru cost from n-1 ... 0
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        # return min dp 0 dp 1
        return min(dp[0], dp[1])