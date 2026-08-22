class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # bf
        # init vars
        n = len(s)
        m = len(p)
        # make dfs
        def dfs(i,j):
            # base case
            # i == n and j == m - return true
            if i == n and j == m:
                return True
            # recursive case
            # compare i and j
            # if j is x* - decision tree
            # need to look at next character
            if j+1 < m and p[j+1] == '*':
                # char at p j and * at j+1
                # while match can either increment i or move on from char at j
                if i < n and (s[i] == p[j] or p[j] == '.'):
                    if dfs(i+1, j):
                        return True
                if dfs(i,j+2):
                    return True
            # if j is . automatic match
            # if j is char = check if match
            elif i < n and j < m and (s[i] == p[j] or p[j] == '.'):
                if dfs(i+1, j+1):
                    return True
            # default case ret false
            return False
        # run dfs
        # return dfs
        return dfs(0,0)