class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # init vars
        res = []
        currset = []
        # make dfs
        def dfs(i, currsum):
            # base case
            # currsum > tar
            if currsum > target:
                return
            # currsum eq tar
            if currsum == target:
                res.append(currset.copy())
                return
            # i oob
            if i == len(nums):
                return
            # recursive case
            # include i - update currset, currsum run dfs i
            currset.append(nums[i])
            dfs(i, currsum+nums[i])
            # skip i - ... no more occurrences of i run dfs i+1
            currset.pop()
            dfs(i+1, currsum)

        # run dfs
        dfs(0,0)
        # return res
        return res