class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # calc len rows, cols
        R, C = len(grid), len(grid[0])
        def dfs(grid, row, col, visited) -> int:
            # base cases
            if row < 0 or col < 0 or \
            row == R or col == C or \
            grid[row][col] == 1 or \
            (row,col) in visited:
                return 0
            
            if row == R-1 and col == C-1:
                return 1

            # recursive cases
            count = 0
            visited.add((row, col))

            count += dfs(grid, row+1, col, visited)
            count += dfs(grid, row-1, col, visited)
            count += dfs(grid, row, col+1, visited)
            count += dfs(grid, row, col-1, visited)
            
            visited.remove((row, col))
            return count
        return dfs(grid, 0, 0, set())