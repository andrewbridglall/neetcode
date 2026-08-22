class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # bottom up soln
        n = len(days)
        # init dp array
        dp = [0]*(n+1)
        # iterate from end to start
        # find min of pass options
        for i in reversed(range(n)):
            dp[i] = float('inf')
            for cost, duration in zip(costs, [1,7,30]):
                j = i
                while j < n and days[j] < days[i] + duration:
                    j+=1
                dp[i] = min(dp[i], cost + dp[j])
        # return dp 0
        return dp[0]