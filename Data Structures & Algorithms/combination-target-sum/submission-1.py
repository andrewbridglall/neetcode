class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, sum, path):
            # base cases
            sum += nums[i]
            if sum > target:
                return
            path.append(nums[i])
            if sum == target:
                res.append(path.copy())
                path.pop()
                return
            # recursive cases
            for ind in range(i, len(nums)):
                dfs(ind, sum, path)
            
            path.pop()
            return
        
        for i in range(len(nums)):
            dfs(i, 0, [])
        return res