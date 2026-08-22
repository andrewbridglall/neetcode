class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #  bf
        # make dfs
        # dfs - come up with all subsets - 1 if subset = t, 0 else
        def dfs(i, currstr):
            # base case
            # if currstr = t
            if currstr == t:
                return 1
            # if i oob
            if i == len(s) or len(currstr) > len(t):
                return 0
            # recusrive case
            count = 0
            # include char i
            count += dfs(i+1, currstr+s[i])
            # skip char i
            count += dfs(i+1, currstr)
            # add counts
            # return counts
            return count

        # run dfs
        return dfs(0, '')