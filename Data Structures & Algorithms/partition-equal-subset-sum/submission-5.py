class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # build memo soln
        if sum(nums) % 2:
            return False
        
        # tar = num // 2
        tar = sum(nums) // 2
        
        # build and init cache
        n,m = len(nums), sum(nums)
        cache = [[-1]*(m+1) for _ in range(n)]
        # make dfs
        def dfs(i, summ):
            # if summ = tar
            if summ == tar:
                return True
            # if i oob
            if i == len(nums):
                return False
            # if in cache return
            if cache[i][summ] != -1:
                return cache[i][summ]
            # recursive case
            # include i
            # skip i
            # set cache val and return val
            cache[i][summ] = (dfs(i+1, summ+nums[i]) or 
                dfs(i+1, summ))
            return cache[i][summ]

        # run dfs and ret
        return dfs(0,0)