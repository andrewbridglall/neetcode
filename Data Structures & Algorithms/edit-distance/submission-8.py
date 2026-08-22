class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp soln
        N, M = len(word1), len(word2)
        dp = [0]*(M+1)
        
        for j in range(M+1):
            dp[j] = len(word2[j:])

        for i in range(N-1, -1, -1):
            currdp = [0]*(M+1)
            currdp[M] = len(word1[i:])
            for j in range(M-1, -1, -1):
                if word1[i] == word2[j]:
                    currdp[j] = dp[j+1]
                else:
                    currdp[j] = 1 + min(currdp[j+1], dp[j], dp[j+1])
            dp = currdp
        return dp[0]
        
