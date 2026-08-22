class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        dp = [0]*(2+len(nums))
        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-1], nums[i-2]+dp[i-2])
        return dp[-1]