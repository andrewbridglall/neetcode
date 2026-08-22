class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l, r
        # if nums[l] == nums[r] move r forward
        # when l neq r, update l = r
        l, r = 0, 0
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[l] == nums[r]:
                r +=1
            l+=1
        return l