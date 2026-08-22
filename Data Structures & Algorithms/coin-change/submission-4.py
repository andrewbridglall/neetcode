class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n,m = len(coins), amount
        dp = [amount+1]*(m+1)

        # init first row
        # coins must add up to amount exactly
        for c in range(m+1):
            if c >= coins[0]:
                # we may add coin(s)
                if c % coins[0] == 0:
                    dp[c] = c//coins[0]
        dp[0] = 0

        # iterate row by row through dp grid
        for i in range(1, n):
            nextdp = [amount+1]*(m+1)
            nextdp[0] = 0
            for c in range(m+1):
                # skip i
                skip = dp[c]
                # include i
                include = amount+1
                if c-coins[i] >= 0:
                    include = 1 + nextdp[c-coins[i]]
                # take min
                nextdp[c] = min(skip, include)
            dp = nextdp
        # return dp n-1 m

        res = dp[m]
        return res if res != amount+1 else -1