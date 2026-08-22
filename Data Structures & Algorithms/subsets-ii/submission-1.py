class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # init vars
        nums.sort()
        res = []
        currset = []
        # make dfs
        def dfs(i):
            # base case
            # i oob - append to res and return
            if i == len(nums):
                res.append(currset.copy())
                return
            # recusrive case
            # include i - run dfs i+1
            currset.append(nums[i])
            dfs(i+1)
            # skip any more occurrences of i
            # currset pop
            currset.pop()
            # while i eq i+1 incr i
            # run dfs i+1
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        # run dfs
        dfs(0)
        # ret res
        return res