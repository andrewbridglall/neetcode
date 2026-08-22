class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # bf
        n = len(nums)
        cache = {}
        # make dfs
        def dfs(i, summ):
            # base case
            # if reached end and summ eq tar
            # if reached end and sum neq tar
            if i == n:
                if summ == target:
                    return 1
                return 0
            if (i,summ) in cache:
                return cache[(i,summ)]
            # recursive case
            # add nums i to sum
            add = dfs(i+1, summ+nums[i])
            # sub nums i from sub
            sub = dfs(i+1, summ-nums[i])
            # return total ways
            cache[(i,summ)] = add + sub
            return add + sub
        # run dfs
        return dfs(0,0)