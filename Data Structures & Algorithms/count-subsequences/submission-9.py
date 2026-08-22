class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp soln
        N, M = len(s), len(t)
        # init dp array
        dp = [[0]*(M+1) for _ in range(N+1)]
        # init base case
        for i in range(N+1):
            dp[i][M] = 1
        # iterate thru dp
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                # num ways with s[i:] and t[j:]
                incl = 0
                if s[i] == t[j]:
                    incl = dp[i+1][j+1]
                skip = dp[i+1][j]
                dp[i][j] = incl + skip
        # return dp 0 0 
        return dp[0][0]
        