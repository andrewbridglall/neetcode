class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        # iterate i thru nums
        for i in range(n):
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
                    res.add((nums[i], nums[j], nums[k]))
                    j +=1
                    k -=1
        # if equal append to res and move ptrs by 1

        # handle dups
        reslist = [[i,j,k] for i,j,k in res]
        return reslist