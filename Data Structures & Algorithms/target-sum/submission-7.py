class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # init ds - n times x all possible sums
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        # grid, row of dicts, single dict
        # init value - 1 ways to get sum 0 with 0 elts
        dp[0][0] = 1
        # calc next row = sum -> iterate through current row plus minus nums i
        for i in range(1, n+1):
            for summ, ways in dp[i-1].items():
                dp[i][summ+nums[i-1]] += ways
                dp[i][summ-nums[i-1]] += ways
            # print(dp[i])
        # ret ds[(n, target)] 
        return dp[n][target]