class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # edge case
        t = sum(nums)
        if t % 2:
            return False
        cache = {}
        # make dfs
        def dfs(i, summ):
            # base case
            if summ > t // 2:
                return False
            if summ == t // 2:
                return True
            if i == len(nums):
                return False
            if (i,summ) in cache:
                return cache[(i,summ)]
            # recursive case
            # incl i
            left = dfs(i+1, summ+nums[i])
            # skip i
            right = dfs(i+1, summ)
            cache[(i,summ)] = left or right
            return left or right
        # run dfs
        return dfs(0,0)
