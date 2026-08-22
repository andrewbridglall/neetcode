class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp soln - space optimized
        M,N = amount, len(coins)

        # init dp array
        dp = [0]*(M+1)
        # base case amount = 0 top left to bottom right
        for n in range(1, N+1):
            currRow = [0]*(M+1)
            currRow[0] = 1
            for m in range(1, M+1):
                # incl
                incl = 0
                if m-coins[n-1] >= 0:
                    incl = currRow[m-coins[n-1]]
                # skip
                skip = dp[m]
                currRow[m] = incl + skip
            dp = currRow
        # return last pos
        return dp[M]