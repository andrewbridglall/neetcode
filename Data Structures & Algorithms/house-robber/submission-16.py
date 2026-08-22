class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0,0,0]
        for i in range(n-1,-1,-1):
            dp[0] = max(nums[i]+dp[2], dp[1])
            # reset
            dp[2] = dp[1]
            dp[1] = dp[0]
            dp[0] = 0
        return dp[1]