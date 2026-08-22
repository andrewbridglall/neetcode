class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp soln
        N,M = len(word1), len(word2)
        # init dp array
        dp = [[0]*(M+1) for _ in range(N+1)]
        # init base case
        for j in range(M+1):
            dp[N][j] = M-j
        for i in range(N+1):
            dp[i][M] = N-i
        # iterate thru dp array
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                # if chars eq
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                # if chars neq
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert, delete, replace)
        # return dp 0 0
        return dp[0][0]