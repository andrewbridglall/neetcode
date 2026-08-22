class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp - space optimize
        dp = [0,0,0]
        n = len(nums)
        for i in range(n):
            dp[2] = max(dp[1], nums[i]+dp[0])
            dp[0] = dp[1]
            dp[1] = dp[2]
        return dp[2]