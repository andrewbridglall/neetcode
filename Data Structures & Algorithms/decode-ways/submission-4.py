class Solution:
    def numDecodings(self, s: str) -> int:
        # if 0 - invalid
        # run dfs
        # implement cache
        cache = {}
        def dfs(i):
            # base case
            # if reach end of str - return 1 - 1 way to reach end
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]
            # recursive case
            # count ways
            count = 0
            # take i - if number in range 1,27 - go to i+1
            if int(s[i]) in range(1,10):
                count += dfs(i+1)
            # take i and i+1 - check i+1 valid, check numer in range
            if int(s[i]) in range(1,10) and i+1 < len(s) and int(s[i:i+2]) in range(1,27):
                count += dfs(i+2)
            # retunr count
            cache[i] = count
            return cache[i]
        
        return dfs(0)