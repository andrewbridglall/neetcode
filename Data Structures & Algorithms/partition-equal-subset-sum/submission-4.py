class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # build set of all possible subset sums
        # target = sum nums //2
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        
        dp = {0}
        
        for n in nums:
            currset = dp.copy()
            for v in dp:
                currset.add(n+v)
            dp = currset
        return target in dp