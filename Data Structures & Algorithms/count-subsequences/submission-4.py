class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # make dfs
        cache = {}
        def dfs(i,j):
            # base case
            # j oob
            if j == len(t):
                return 1
            # i oob
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # chars eq
            # chars neq
            count = dfs(i+1, j)
            if s[i] == t[j]:
                count += dfs(i+1, j+1)
            cache[(i,j)] = count
            return cache[(i,j)]
            
        # ret dfs
        return dfs(0,0)