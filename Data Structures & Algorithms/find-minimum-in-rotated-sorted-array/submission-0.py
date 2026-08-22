class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if l > r we know largest and smallest are in range
        # target = min
        l,r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
            
        while l < r:
            if r == l+1:
                break
            # get mid
            m = (l+r)//2
            # check l - mid
            if nums[l] > nums[m]:
                r = m
            # check mid - r
            elif nums[m] > nums[r]:
                l = m
        return nums[r]

