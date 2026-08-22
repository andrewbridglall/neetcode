class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # init res
        res = []
        charCodes = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        # build dfs
        def dfs(i, currstr):
            # base case
            if i == len(digits):
                res.append(currstr)
                return
            # recursive case
            for c in charCodes[int(digits[i])]:
                dfs(i+1, currstr+c)
        # run dfs
        dfs(0, "")
        # return res
        return res