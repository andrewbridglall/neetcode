class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        window = {nums[L]}
        for R in range(1, len(nums)):
            if R-L+1 > k+1:
                window.remove(nums[L])
                L +=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False