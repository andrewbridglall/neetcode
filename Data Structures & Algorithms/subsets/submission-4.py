class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init vars
        res = []
        currset = []
        # run dfs
        def dfs(i):
            # base case
            # i oob - return currset copy
            if i == len(nums):
                res.append(currset.copy())
                return
            # recursive case
            # include i
            currset.append(nums[i])
            dfs(i+1)
            # skip i
            currset.pop()
            dfs(i+1)
        # return res
        dfs(0)
        return res
