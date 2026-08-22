class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp soln
        # init vars
        n = len(nums)
        dp = [0]*n
        # fill in dp arr from end to start
        for i in range(n-2, -1, -1):
            # calc min steps from i to n-1
            minSteps = float('inf')
            for j in range(nums[i], 0, -1):
                nextIndex = min(i+j, n-1)
                minSteps = min(minSteps, 1 + dp[nextIndex])
            dp[i] = minSteps
        # calc min steps to reach n-1 from i
        # return dp 0
        return dp[0]