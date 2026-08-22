class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # declare and init currlen and maxlen
        if len(nums) < 2:
            return len(nums)
        currLen, maxLen = 1, 0
        nums.sort()
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1]:
                continue
            elif nums[r] == nums[r-1]+1:
                currLen +=1
            else:
                currLen = 1
            maxLen = max(currLen, maxLen)
        maxLen = max(currLen, maxLen)
        return maxLen

        # sort arr
        # set start to i=0
        # check if nums i+1 is consecutive
        # if == skip
        # if nums[i+1] = nums[i] +1 : update currleng
        # maxlen = max(maxleng, currleng)
        # else: start over = set start to r
                