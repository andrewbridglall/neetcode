class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            target = (-1)*nums[i]
            # handle dups at i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l]+nums[r] < target:
                    l+=1
                elif nums[l]+nums[r] > target:
                    r-=1
                else:
                    # match found - add to res
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l-1] == nums[l] and l < r:
                        l+=1
        return res