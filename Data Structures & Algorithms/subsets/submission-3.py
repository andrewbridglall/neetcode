class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subsetHelper(i, currSet, res):
            # base case
            if i == len(nums):
                res.append(currSet.copy())
                return
            # recursive case
            # include and run dfs
            currSet.append(nums[i])
            subsetHelper(i+1, currSet, res)
            # skip and run dfs
            currSet.pop()
            subsetHelper(i+1, currSet, res)
        subsetHelper(0, [], res)
        return res