class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp soln
        n = len(nums)
        # dp stores max profit at given pos
        dp = [0]*(n+1)
        # fill in base cases - n-1, n-2
        dp[n-1] = nums[n-1]
        # dp i = max(houses i + dp i+2, dp i+1)
        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])
        return dp[0]