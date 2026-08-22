class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # optimal
        n = len(nums)
        allnums = 0
        for i in range(n+1):
            allnums += i
        currsum = sum(nums)
        return allnums - currsum