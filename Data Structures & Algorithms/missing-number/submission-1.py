class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = {i for i in range(n+1)}
        for n in nums:
            s.remove(n)
        for item in s:
            return item