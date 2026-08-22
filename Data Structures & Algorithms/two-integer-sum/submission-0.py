class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # design dict val:index
        # for n in nums, check if target-n is in dict, if so, return i, j
        hm = {n:i for i,n in enumerate(nums)}
        for i,n in enumerate(nums):
            if target-n in hm and i < hm[target-n]:
                return [i, hm[target-n]]
        return None