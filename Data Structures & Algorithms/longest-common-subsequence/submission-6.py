class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # run dfs
        cache = {}
        def dfs(i,j):
            # base case
            # i or j oob
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # s1 i == s2 j
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            # i j neq
            res1 = dfs(i+1, j)
            res2 = dfs(i, j+1)
            cache[(i,j)] = max(res1, res2)
            return cache[(i,j)]
        # return dfs
        return dfs(0,0)