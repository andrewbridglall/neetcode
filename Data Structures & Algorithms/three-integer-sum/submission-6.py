class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init vars
        nums.sort()
        n = len(nums)
        res = []
        # iter i
        for i in range(n):
            # handle i edge cases
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tar = -1 * nums[i]
            j, k = i+1, n-1
            while j < k:
                # handle j edge cases
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                summ = nums[j] + nums[k]
                if summ > tar:
                    k -=1
                elif summ < tar:
                    j +=1
                else: # ==
                    res.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1


        # return res
        return res