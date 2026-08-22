class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # init vars
        letters = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        res = []
        
        # make dfs
        def dfs(i, currstr):
            # base case
            if i == len(digits):
                res.append(currstr)
                return
            # recursive case
            for s in letters[digits[i]]:
                dfs(i+1, currstr+s)

        # run dfs
        dfs(0, '')
        # return res
        return [] if not digits else res