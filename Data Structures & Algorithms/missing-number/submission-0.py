class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor all numbers together
        res = 0
        n = len(nums)
        for i in range(n+1):
            res = res ^ i
        
        for n in nums:
            res = res ^ n
        
        return res