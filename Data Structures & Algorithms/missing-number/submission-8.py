class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # optimal
        # xor
        n = len(nums)
        res = 0
        # iter thru all possible values - xor
        for i in range(n+1):
            res ^= i
        # iter thru all nums in nums -xor
        for num in nums:
            res ^= num
        # return res
        return res