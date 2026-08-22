class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bf - decision tree
        # init vars
        n = len(prices)
        cache = {}
        # make dfs
        def dfs(i, hasCoin):
            # base case
            if i >= n:
                return 0 # if oob no more additional profit or loss
            if (i, hasCoin) in cache:
                return cache[(i, hasCoin)]
            # recursive case
            # buy - only if don't have coin
            if not hasCoin:
                buy = -1*prices[i] + dfs(i+1, 1)
                skip_buy = dfs(i+1, 0)
                cache[(i, hasCoin)] = max(buy, skip_buy) 
                return max(buy, skip_buy)
            # sell - only if have coin
            else:
                sell = prices[i] + dfs(i+2, 0)
                skip_sell = dfs(i+1, 1)
                cache[(i, hasCoin)] = max(sell, skip_sell) 
                return max(sell, skip_sell)
            # return max profit
            
        # run dfs
        return dfs(0, 0)