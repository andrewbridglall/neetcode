class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # bf
        # make dfs
        def dfs(i,j):
            # base case
            # if i == n
            if i == len(word1):
                return len(word2) - j
            # if j == m
            if j == len(word2):
                return len(word1) - i
            # recursive case 
            # if chars match
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            # if chars neq
            # insert
            insert = 1 + dfs(i, j+1)
            # delete
            delete = 1 + dfs(i+1, j)
            # replace
            replace = 1 + dfs(i+1, j+1)
            # ret min operations
            return min(insert, delete, replace)
        # run dfs
        return dfs(0,0)