class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bf - optimize runtime
        # init set
        numset = set()
        n = len(nums)
        for i in range(n+1):
            numset.add(i)
        # iterate thru nums and remove from set
        for n in nums:
            numset.remove(n)
        # convert to list and return only elt
        return list(numset)[0]
