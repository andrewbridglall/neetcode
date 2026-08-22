class Solution:
    def rob(self, nums: List[int]) -> int:
        # helper
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def robhelper(l,r):
            # edge case
            if l == r:
                return nums[0]
            dp = [0,0,0]
            for i in range(l,r):
                dp[2] = max(dp[1], nums[i]+dp[0])
                dp[0] = dp[1]
                dp[1] = dp[2]
            return dp[2]
        return max(robhelper(0,n-1), robhelper(1,n))