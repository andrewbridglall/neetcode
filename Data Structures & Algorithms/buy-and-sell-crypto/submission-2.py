class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        maxP = 0
        for s in range(1, len(prices)):
            maxP = max(maxP, prices[s]-prices[b])
            if prices[s] < prices[b]:
                b = s
        return maxP