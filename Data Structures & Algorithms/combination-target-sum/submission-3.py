class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # define dfs
        def dfs(i, currset, currsum):
            # base case
            # if sum = target - append copy of currset to res and ret
            # if sum > target or i oob return
            if currsum == target:
                res.append(currset.copy())
                return
            if currsum > target or i == len(nums):
                return
            # recursive case
            # choose i again and call dfs
            currset.append(nums[i])
            dfs(i, currset, currsum+nums[i])
            # pop i
            # call dfs at i+1
            currset.pop()
            dfs(i+1, currset, currsum)

        # run dfs
        dfs(0, [], 0)
        # return res
        return res