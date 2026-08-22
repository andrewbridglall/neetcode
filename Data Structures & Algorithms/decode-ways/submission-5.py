class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # make dfs
        def dfs(i):
            # base case
            if i == n:
                return 1
            if i > n or int(s[i]) == 0:
                return 0
            # recursive case
            # count
            count = 0
            # only if valid continue tree**
            # include i go to i+1
            if int(s[i]) in range(1,27):
                count += dfs(i+1)
            # take i,i+1 go to i+2
            if i+1 < n and int(s[i:i+2]) in range(1,27):
                count += dfs(i+2)
            # ret count
            return count
        # run dfs
        # return
        return dfs(0)