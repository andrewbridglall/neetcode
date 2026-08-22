class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # build cache
        cache = [{} for _ in range(len(nums))]
        # build dfs
        def dfs(i, summ):
            # base case
            # if i oob
            # if sum reached target
            if i == len(nums):
                return 1 if summ == target else 0
            # if found in cache return
            if summ in cache[i]:
                return cache[i][summ]
            # recursive case
            count = 0
            # add pos nums i and run dfs
            count += dfs(i+1, summ+nums[i])
            # add neg nums i and run dfs
            count += dfs(i+1, summ+(-1)*nums[i])
            # return total count
            # add result to cache
            cache[i][summ] = count
            # return val in cache
            return cache[i][summ]

        # run dfs
        # return
        return dfs(0, 0)