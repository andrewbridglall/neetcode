class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif nums[l] <= nums[m]:
                if target in range(nums[l], nums[m]):
                    r = m-1
                else:
                    l = m+1
            elif nums[m] <= nums[r]:
                if target in range(nums[m]+1, nums[r]+1):
                    l = m+1
                else:
                    r = m-1
        return -1