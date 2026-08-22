class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp soln - space optimized
        n = len(nums)
        # init dp
        dp = defaultdict(int)

        # iterate through dp ds
        dp[0] = 1
        for i in range(1, n+1):
            currdp = defaultdict(int)
            for summ in dp:
                currdp[summ+nums[i-1]] += dp[summ]
                currdp[summ-nums[i-1]] += dp[summ]
            dp = currdp
        # return
        return dp[target]