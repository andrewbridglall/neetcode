class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp soln - space optimized
        # init vars
        n = len(prices)
        dp = [[0]*(3) for _ in range(2)]
        # iterate thru dp array
        for i in range(n-1, -1, -1):
            # fill in max profit for both buy and sell at i
            # buy - assumes no coin at i
            buy = -1*prices[i] + dp[1][1]
            skip_buy = dp[0][1]
            dp[0][0] = max(buy, skip_buy)
            # sell - assumes coin at i
            sell = prices[i] + dp[0][2]
            skip_sell = dp[1][1]
            dp[1][0] = max(sell, skip_sell)

            # update dp 1 2 for row 0
            dp[0][2] = dp[0][1]
            dp[0][1] = dp[0][0]
            # update dp 1 2 for row 1
            dp[1][2] = dp[1][1]
            dp[1][1] = dp[1][0]
        # ret dp 0 0
        return dp[0][0]