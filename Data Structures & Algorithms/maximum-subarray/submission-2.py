class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # optimal
        # kadanes

        # init vars
        maxsum = nums[0]
        currsum = 0
        # iter thru nums
        for n in nums:
            currsum = max(currsum, 0)
            currsum += n
            maxsum = max(maxsum, currsum)
        # update currsum and max
        # return max
        return maxsum