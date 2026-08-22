class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # bf soln
        n = len(nums)
        # make dfs
        def dfs(i):
            # base case
            if i >= n-1:
                return True
            if nums[i] == 0:
                return False
            # recursive caes
            # max jump = nums i
            for jump in range(nums[i], 0, -1):
                if dfs(i+jump):
                    return True
            return False
        # run dfs
        return dfs(0)