class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # init vars
        N,M = len(text1), len(text2)
        # init dp array
        # init base case rows cols
        dp = [[0]*(M+1) for _ in range(N+1)]
        # iterate thru dp and fill in
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                # if i j eq
                if text1[i] == text2[j]:
                   dp[i][j] = 1+dp[i+1][j+1]
                # else
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp 0 0
        return dp[0][0]