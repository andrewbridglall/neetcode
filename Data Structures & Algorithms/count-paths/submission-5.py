class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bf - dfs
        # init vars
        cache = {}
        visit = set()
        # make dfs
        def dfs(r,c):
            # base case
            if r == m-1 and c == n-1:
                return 1
            if r not in range(m) or c not in range(n) or (r,c) in visit:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            # recursive case
            visit.add((r,c))
            count = 0
            count += dfs(r+1, c)
            count += dfs(r, c+1)
            visit.remove((r,c))
            cache[(r,c)] = count
            return count
        # run dfs
        return dfs(0,0)