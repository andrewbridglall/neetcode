class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # init vars
        candidates.sort()
        n = len(candidates)
        res = set()
        currset = []
        # make dfs
        def dfs(i, target):
            # base case
            # target == 0
            if target == 0:
                res.add(tuple(currset))
                return
            # target < 0
            # i == n and target neq 0 or < 0 - return
            if target < 0 or i ==n:
                return
            # recursive case
            # incl i
            currset.append(candidates[i])
            dfs(i+1, target - candidates[i])
            # skip i
            currset.pop()
            dfs(i+1, target)
        # run dfs
        dfs(0, target)
        # return res
        # convert res to list
        return [list(item) for item in res]