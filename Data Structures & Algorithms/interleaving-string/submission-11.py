class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # run dfs
        cache = {}

        def dfs(i,j):
            # base case
            k = i+j
            # if k == len s3 and i == len s1 and j == len s2
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # if s1 i == s3 k
            # res = False
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1,j):
                    return True
            # if s2 j == s3 k
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1):
                    return True
            
            # ret false if none eq
            cache[(i,j)] = False
            return cache[(i,j)]

        # return dfs
        return dfs(0,0)