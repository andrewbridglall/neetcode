class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -1*float('inf')
        b,s = 0,1
        while b < len(prices) and s < len(prices):
            profit = max(profit, prices[s]-prices[b])
            if prices[s] < prices[b]:
                b = s
            s+=1
        return profit if profit > 0 else 0