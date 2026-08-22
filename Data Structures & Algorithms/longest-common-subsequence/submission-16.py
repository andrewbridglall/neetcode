class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bf
        M, N = len(text1), len(text2)
        cache = {}
        # make dfs
        def dfs(i,j):
            # base case
            if i == M or j == N:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            if text1[i] == text2[j]:
                return 1+dfs(i+1,j+1)
            cache[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
            return max(dfs(i+1,j), dfs(i, j+1))
        # run dfs
        return dfs(0,0)