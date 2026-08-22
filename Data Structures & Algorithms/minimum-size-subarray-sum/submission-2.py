class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minLen = len(nums)+1
        total = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minLen = min(minLen, R-L+1)
                total -= nums[L]
                L +=1
        return minLen if minLen != len(nums)+1 else 0
