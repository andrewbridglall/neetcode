class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp soln
        M, N = len(text1), len(text2)
        
        dp = [0]*(N+1)
        for i in range(M-1, -1, -1):
            currRow = [0]*(N+1)
            for j in range(N-1, -1 ,-1):
                # if eq
                if text1[i] == text2[j]:
                    currRow[j] = 1 + dp[j+1]
                # else (neq)
                else:
                    currRow[j] = max(dp[j], currRow[j+1])
            dp = currRow
        return dp[0]

        