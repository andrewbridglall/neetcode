class Solution:
    def rob(self, nums: List[int]) -> int:
        # implement house robber
        # run func from 0 to n-2, then 1 to n-1
        n = len(nums)
        if n == 1:
            return nums[0]
            
        def robber(l,r):
            if r < l:
                return 0
            arr = nums[l:r+1]
            n = len(arr)
            dp = [0,0,0]
            for i in range(n-1, -1,-1):
                dp[0] = max(arr[i]+dp[2], dp[1])
                # reset
                dp[2] = dp[1]
                dp[1] = dp[0]
            return dp[0]
        return max(robber(0,n-2), robber(1,n-1))