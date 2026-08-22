class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking optimized
        # init vars
        candidates.sort()
        n = len(candidates)
        currset = []
        res = []
        # make dfs
        def dfs(i, summ):
            # base case
            # target reached
            if summ == target:
                res.append(currset.copy())
                return
            # target exceeded
            # i oob
            if summ > target or i == n:
                return
            # recusrive case
            # incl i (can inlcude dup) - at most ...
            currset.append(candidates[i])
            dfs(i+1, summ + candidates[i])
            # skip i - if dup -skip all remainig occurrences of i
            currset.pop()
            while i < n-1 and candidates[i] == candidates[i+1]:
                i +=1
            dfs(i+1, summ)

        # run dfs
        dfs(0, 0)
        # return res
        return res