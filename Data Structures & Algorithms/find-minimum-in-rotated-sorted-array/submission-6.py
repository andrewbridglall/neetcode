class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the pivot
        l,r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            # base case
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            if nums[m] <= nums[r]:
                res = min(res, nums[m])
                r = m-1
            elif nums[l] <= nums[m]:
                res = min(res, nums[l])
                l = m+1
            # iterative case
        return res