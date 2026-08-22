class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # build dfs
        def dfs(i, summ):
            # base case
            # if i oob
            # if sum reached target
            if i == len(nums):
                if summ == target:
                    return 1
                return 0
            # recursive case
            count = 0
            # add pos nums i and run dfs
            count += dfs(i+1, summ+nums[i])
            # add neg nums i and run dfs
            count += dfs(i+1, summ+(-1)*nums[i])
            # return total count
            return count

        # run dfs
        # return
        return dfs(0, 0)