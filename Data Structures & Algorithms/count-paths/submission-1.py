class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1]*n for _ in range(m)]

        def mem(r, c, cache):
            # base cases
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if cache[r][c] != -1:
                return cache[r][c]

            # recursive case
            cache[r][c] = mem(r+1, c, cache) + mem(r, c+1, cache)
            return cache[r][c]
        
        return mem(0,0, cache)