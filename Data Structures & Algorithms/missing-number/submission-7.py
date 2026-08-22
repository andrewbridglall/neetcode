class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bf - hashset
        # add nums to numset
        n = len(nums)
        numset = {n for n in nums}
        # iter thru total range
        for i in range(n+1):
        # if elt not found in num set - found missing number
            if i not in numset:
                return i
        # return