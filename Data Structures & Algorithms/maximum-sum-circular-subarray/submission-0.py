class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxsum = nums[0]
        for i in range(n):
            sum = 0
            for j in range(i, i+n):
                sum += nums[j%n]
                maxsum = max(maxsum, sum)
        return maxsum

