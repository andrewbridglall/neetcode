class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init vars
        l,r = 0, len(nums)-1
        # binary search
        while l <= r:
            # calc mid
            mid = (l+r)//2
            # if targ == mid
            if target == nums[mid]:
                return mid
            # if pivot in left half
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            # if pivot in right half
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
                

        # ret index if exists
        return -1