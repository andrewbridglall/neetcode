class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # run dfs
        def dfs(i):
            # base case
            # if reached last index - ret true
            if i >= len(nums)-1:
                return True
            # recursive case
            reachEnd = False
            # try all jump distances <= nums i
            for dist in range(1, nums[i]+1):
                reachEnd |= dfs(i+dist)
            # if one path is true, return true
            return reachEnd
        
        return dfs(0)