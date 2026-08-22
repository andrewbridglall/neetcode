class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # init vars
        res = nums[0]
        # iterate through nums
        # keep track of currmax, currmin
        # if num == 0 reset currmax, currmin to 1, check if res = 0
        currmax, currmin = 1, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                currmax = currmin = 1
                res = max(res, 0)
                continue
            # update currmax
            tmp = currmax
            currmax = max(currmax*nums[i], currmin*nums[i], nums[i])
            # update currmin
            currmin = min(tmp*nums[i], currmin*nums[i], nums[i])
            # update max
            res = max(res, currmax)
        return res