class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # init vars
        res = []
        currset = []
        stack = []
        # make dfs
        def dfs(i):
            # base case
            # if i == 2n and stack is empty - valid add to res
            if i == 2*n:
                if not stack:
                    res.append("".join(currset))
                return
            # recursive case
            # append (
            currset.append('(')
            stack.append('(')
            dfs(i+1)
            
            currset.pop()
            stack.pop()
            
            # append )
            if stack and stack[-1] == '(':
                stack.pop()
                currset.append(')')
                dfs(i+1)
                
                # reset
                stack.append('(')
                currset.pop()


        # run dfs
        dfs(0)
        # ret res
        return res