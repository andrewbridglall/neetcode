class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # bf
        # init vars
        n = len(nums)
        maxsum = nums[0]
        # calc all subarrays
        for i in range(n):
            currsum = 0
            for j in range(i,n):
                # calc summ and track max
                currsum += nums[j]
                maxsum = max(maxsum, currsum)
        # return max
        return maxsum