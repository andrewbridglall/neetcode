class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = currmin = nums[0]
        globalmax = currmax
        n = len(nums)
            
        for i in range(1, n):
            tmp = currmax
            currmax = max(currmax*nums[i], nums[i], currmin*nums[i])
            currmin = min(tmp*nums[i], nums[i], currmin*nums[i])
            globalmax = max(globalmax, currmax)
        return globalmax