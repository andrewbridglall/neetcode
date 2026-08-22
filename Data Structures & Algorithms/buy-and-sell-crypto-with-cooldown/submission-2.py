class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp soln
        # init vars
        n = len(prices)
        dp = defaultdict(int)
        # iterate thru dp array
        for i in range(n-1, -1, -1):
            # fill in max profit for both buy and sell at i
            # buy - assumes no coin at i
            buy = -1*prices[i] + dp[(i+1, 1)]
            skip_buy = dp[(i+1, 0)]
            dp[(i, 0)] = max(buy, skip_buy)
            # sell - assumes coin at i
            sell = prices[i] + dp[(i+2, 0)]
            skip_sell = dp[(i+1, 1)]
            dp[(i, 1)] = max(sell, skip_sell)    
        # ret dp 0 0
        return dp[(0,0)]