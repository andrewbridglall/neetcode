class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # iterate i thru nums
        i = 0
        while i < n:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
        # target = -1 * nums i
            target = -1 * nums[i]
            j = i+1
            k = n-1
            while j < k:
        # set ptrs j, k
        # compare and update
                summ = nums[j]+nums[k]
                if summ > target:
                    k -=1
                elif summ < target:
                    j +=1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j +=1
                    k -=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
        # if equal append to res and move ptrs by 1
        # handle dups
            i+=1
        return res