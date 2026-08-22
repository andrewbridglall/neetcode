class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # run dfs
        # memo
        cache = {}
        def dfs(i, j):
            # base case
            # i or j oob
            if i == len(text1) or j == len(text2):
                return 0 #no more common subsequences
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # s1 i eq s2 j - 1 + dfs(i+1, j+1)
            res = 0
            if text1[i] == text2[j]:
                res = 1+dfs(i+1,j+1)
            # else neq
            else:
            # i+1, j
            # i, j+1
            # return max
                left = dfs(i+1, j)
                right = dfs(i, j+1)
                res = max(res, left, right)
            cache[(i,j)] = res
            return cache[(i,j)]

        # return dfs
        return dfs(0,0)