class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # run dfs
        # memo
        cache = {}
        def dfs(i):
            # base case
            # if reached last index - ret true
            if i >= len(nums)-1:
                return True
            if i in cache:
                return cache[i]
            # recursive case
            reachEnd = False
            # try all jump distances <= nums i
            for dist in range(1, nums[i]+1):
                reachEnd |= dfs(i+dist)
            # if one path is true, return true
            cache[i] = reachEnd
            return cache[i]
        
        return dfs(0)