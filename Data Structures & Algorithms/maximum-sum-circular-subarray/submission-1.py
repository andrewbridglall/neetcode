class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # get max
        gmax = nums[0]
        currmax = 0

        # get min
        gmin = nums[0]
        currmin = 0

        # get total
        total = 0

        for n in nums:
            currmax = max(currmax, 0)
            currmax+=n
            gmax = max(gmax, currmax)

            currmin = min(currmin, 0)
            currmin+=n
            gmin = min(gmin, currmin)

            total +=n
        
        return max(gmax, total-gmin) if gmax > 0 else gmax