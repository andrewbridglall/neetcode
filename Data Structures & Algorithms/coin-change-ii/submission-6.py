class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp - space optimized
        n,m = len(coins), amount
        # init dp array
        dp = [0]*(m+1)
        # # fill in first col and row
        # dp[0] = 1
        # for c in range(1, m+1):
        #     if c >= coins[0] and c % coins[0] == 0:
        #         dp[c] = 1
        # traverse dp grid
        for i in range(n):
            currRow = [0]*(m+1)
            currRow[0] = 1
            for c in range(1, m+1):
                # skip i
                skip = dp[c]
                # include i
                include = 0
                if c-coins[i] >= 0:
                    include = currRow[c-coins[i]]
                # add both
                currRow[c] = skip+include
            dp = currRow
        # return last index
        return dp[m]