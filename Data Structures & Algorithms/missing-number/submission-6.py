class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bf
        # sort nums
        n = len(nums)
        nums.sort()
        # iter thru 0..n and check for missing number
        for i in range(n+1):
            # nums i should be i
            if i == n:
                return n
            if nums[i] != i:
                return i
        # return mising number