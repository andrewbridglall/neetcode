class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        for r in range(len(nums)-1, 0, -1):
            if nums[r] == nums[r-1]:
                nums.pop(r)
        print(nums)
        return len(nums)