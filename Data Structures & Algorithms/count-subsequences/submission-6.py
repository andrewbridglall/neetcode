class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N,M = len(s), len(t)
        dp = [0]*(M+1)
        dp[M] = 1
        
        for i in range(N-1, -1, -1):
            # currdp
            currdp = [0]*(M+1)
            currdp[M] = 1
            for j in range(M-1, -1, -1):
                currdp[j] = dp[j]
                if s[i] == t[j]:
                    currdp[j] += dp[j+1]
            dp = currdp
        return dp[0]      
        