class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currsum, currset):
            # base case
            # if i oob return
            if currsum > target:
                return
            # if currsum == target append currset
            if currsum == target and currset not in res:
                res.append(currset.copy())
                return

            # recursive case
            # include i again
            currsum += nums[i]
            currset.append(nums[i])
            dfs(i, currsum, currset)
            
            currsum -= nums[i]
            currset.pop()
            
            # include i+1
            if i+1 < len(nums):
                currsum += nums[i+1]
                currset.append(nums[i+1])
                dfs(i+1, currsum, currset)

            # skip i+1
            if i+1 < len(nums):
                currsum -= nums[i+1]
                currset.pop()
                dfs(i+1, currsum, currset)
        
        dfs(0, 0, [])
        return res