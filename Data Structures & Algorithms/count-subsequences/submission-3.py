class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # make dfs
        def dfs(i,j):
            # base case
            # j oob
            if j == len(t):
                return 1
            # i oob
            if i == len(s):
                return 0
            # recursive case
            # chars eq
            # chars neq
            count = dfs(i+1, j)
            if s[i] == t[j]:
                count += dfs(i+1, j+1)
            return count
            
        # ret dfs
        return dfs(0,0)