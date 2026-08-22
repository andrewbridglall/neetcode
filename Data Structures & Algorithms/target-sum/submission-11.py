class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp soln
        n = len(nums)
        # init dp
        dp = [defaultdict(int) for _ in range(n+1)]
        # iterate through dp ds
        dp[0][0] = 1
        for i in range(1, n+1):
            for summ in dp[i-1]:
                dp[i][summ+nums[i-1]] += dp[i-1][summ]
                dp[i][summ-nums[i-1]] += dp[i-1][summ]
        # return
        return dp[n][target]