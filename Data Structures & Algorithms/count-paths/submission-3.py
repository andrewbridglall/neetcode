class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # declare prevRow, currRow
        # fill in currRow cell from sum of down and right
        # iterate across currRow
        # then move a level up

        # prevRow = [0]*n
        currRow = [0]*n
        currRow[n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-2, -1, -1):
                currRow[c] += currRow[c+1]
            # prevRow = currRow
        return currRow[0]