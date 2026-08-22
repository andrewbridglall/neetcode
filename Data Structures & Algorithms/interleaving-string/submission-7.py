class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # make dfs
        cache = {}
        def dfs(i,j):
            # base case
            # if reached end of s3
            k = i+j
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            left, right = False, False
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1,j):
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1):
                    return True
            cache[(i,j)] = False
            return cache[(i,j)]

        # run dfs
        return dfs(0,0)