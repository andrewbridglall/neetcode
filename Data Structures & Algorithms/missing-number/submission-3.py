class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bf
        # sort array
        nums.sort()
        # iter thru nums, elt should start at 0
        elt = 0
        for n in nums:
            if elt != n:
                return elt
            elt +=1
        # increment elt and check if found
        # if not found - return elt
        # if reach end return elt
        return elt