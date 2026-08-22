class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum2 = 0
        for i in range(len(nums)+1):
            sum2 += i
        sum1 = sum(nums)
        return sum2-sum1