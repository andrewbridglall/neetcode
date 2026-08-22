class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp soln
        N,M = len(text1), len(text2)
        dp = [0]*(M+1)

        for i in range(N-1, -1, -1):
            currdp = [0]*(M+1)
            for j in range(M-1, -1 ,-1):
                # recursive case
                # s1 i == s2 j
                if text1[i] == text2[j]:
                    currdp[j] = 1 + dp[j+1]
                # i j neq
                else:
                    currdp[j] = max(dp[j], currdp[j+1])
            dp = currdp
        
        return dp[0]