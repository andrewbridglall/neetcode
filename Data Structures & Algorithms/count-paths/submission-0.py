class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c):
            # base cases
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            # recursive case
            count = 0
            count += dfs(r+1, c)
            count += dfs(r, c+1)
            return count
        return dfs(0,0)