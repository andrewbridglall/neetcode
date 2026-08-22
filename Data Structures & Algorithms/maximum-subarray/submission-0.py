class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cursum = nums[0], 0

        for num in nums:
            cursum = max(cursum, 0)
            cursum += num
            maxsum = max(maxsum, cursum)
        return maxsum