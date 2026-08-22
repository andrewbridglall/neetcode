class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init vars
        l,r = 0, len(nums)-1
        minn = nums[0]
        # while l <= r
        while l <= r:
            # get mid
            m = (l+r)//2
            # save mid
            minn = min(minn, nums[m])
            # if pivot in left half
            if nums[l] > nums[m]:
                r = m-1
            # if pivot in right right
            elif nums[m] > nums[r]:
                l = m+1
            # else
            else:
                minn = min(minn, nums[l])
                break
        
        # return min
        return minn