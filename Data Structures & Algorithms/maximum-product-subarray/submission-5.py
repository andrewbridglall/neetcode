class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = 1
        currmin = 1
        globalmax = nums[0]
        n = len(nums)
            
        for i in range(n):
            tmp = currmax
            currmax = max(currmax*nums[i], nums[i], currmin*nums[i])
            currmin = min(tmp*nums[i], nums[i], currmin*nums[i])
            globalmax = max(globalmax, currmax)
        return globalmax