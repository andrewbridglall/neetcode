class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # init vars
        N, M, K = len(s1), len(s2), len(s3)
        cache = {}
        if N+M != K:
            return False
        # make dfs
        def dfs(i,j,k):
            # base case
            if i == N and j == M and k == K:
                return True
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            # recursive case
            if i < N and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    return True
            if j < M and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    return True
            cache[(i,j,k)] = False
            return False

        # run dfs
        return dfs(0,0,0)