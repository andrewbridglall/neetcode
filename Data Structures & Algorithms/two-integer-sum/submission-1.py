class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,n in enumerate(nums):
            if target-n in hm and hm[target-n] != i:
                return [hm[target-n], i]
            hm[n] = i
        return None