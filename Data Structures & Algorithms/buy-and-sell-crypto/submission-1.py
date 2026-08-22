class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        maxP = -1*float('inf')
        l = 0
        for r in range(1, len(prices)):
            maxP = max(maxP, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxP if maxP > 0 else 0
