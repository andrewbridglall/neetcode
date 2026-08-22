class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp soln - space optimized
        N,M = len(word1), len(word2)
        # init dp array
        dp = [0]*(M+1)
        # init base case
        for j in range(M+1):
            dp[j] = M-j
        
        # iterate thru dp array
        for i in range(N-1, -1, -1):
            currdp = [0]*(M+1)
            currdp[M] = N-i
            for j in range(M-1, -1, -1):
                # if chars eq
                if word1[i] == word2[j]:
                    currdp[j] = dp[j+1]
                # if chars neq
                else:
                    insert = 1 + currdp[j+1]
                    delete = 1 + dp[j]
                    replace = 1 + dp[j+1]
                    currdp[j] = min(insert, delete, replace)
            dp = currdp
        # return dp 0 0
        return dp[0]