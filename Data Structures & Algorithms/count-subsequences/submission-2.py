class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # run dfs
        cache = {}
        def dfs(i,j):
            # base case
            # if j oob
            if j == len(t):
                return 1
            # if i oob
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # if chars eq
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            # if chars neq
            else:
                cache[(i,j)] = dfs(i+1, j)
            return cache[(i,j)]
        # return dfs
        return dfs(0,0)