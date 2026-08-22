class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # bf
        # make dfs
        # can cache since output depends only on pos i,j
        cache = {}
        def dfs(i,j):
            # base case
            # j oob on t - found valid subsequence - ret 1
            if j == len(t):
                return 1
            # i oob on s - reached end of s no more subseq - ret 0
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # if i eq j - 'take' i and go to i+1, j+1
            incl = 0
            if s[i] == t[j]:
                incl = dfs(i+1,j+1)
            # or skip i - go to i+1, j stays
            skip = dfs(i+1, j)
            # return cumul. res
            cache[(i,j)] = incl + skip
            return incl + skip
        # run dfs
        return dfs(0,0)