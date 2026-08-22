class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # init vars
        # choose min(text1, text1) for len of row
        s1 = s2 = None
        if len(text1) > len(text2):
            s1 = text1
            s2 = text2
        else:
            s1 = text2
            s2 = text1
        N,M = len(s1), len(s2)
        
        # init dp array
        # init base case rows cols
        dp = [0]*(M+1) #i+1
        # iterate thru dp and fill in
        for i in range(N-1, -1, -1):
            currRow = [0]*(M+1)
            for j in range(M-1, -1, -1):
                # if i j eq
                if s1[i] == s2[j]:
                   currRow[j] = 1+dp[j+1]
                # else
                else:
                    currRow[j] = max(dp[j], currRow[j+1])
            dp = currRow
        # return dp 0 0
        return dp[0]