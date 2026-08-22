class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R,C = len(obstacleGrid), len(obstacleGrid[0])

        curRow = [0]*C
        curRow[C-1] = 1

        for r in range(R-1, -1, -1):
            if obstacleGrid[r][C-1] == 1:
                curRow[C-1] = 0
            for c in range(C-2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] += curRow[c+1]
        return curRow[0]