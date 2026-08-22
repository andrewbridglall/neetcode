class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        # bf soln
        # run dfs
        def dfs(i, lastNum):
            # base case
            # if i oob - return 1
            if i == len(s):
                return 1
            # if lastnum invalid - return 0
            # recursive case
            # count valid paths to end
            count = 0
            # append number
            if int(s[i]) in range(1,27):
                count += dfs(i+1, s[i])
            # combine with lastnum
            if int(lastNum+s[i]) in range(1,27):
                count += dfs(i+1, lastNum+s[i])
            # return count
            return count
        
        return dfs(1, s[0])
