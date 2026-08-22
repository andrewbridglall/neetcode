class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # init hashset
        numSet = set(nums)
        maxLen = 0
        # for n in set
        for n in numSet:
            currlen = 0
            if n-1 not in numSet:
                currlen = 1
                target = n+1
                while target in numSet:
                    currlen+=1
                    target +=1
                maxLen = max(maxLen, currlen)
        return maxLen
        # if n-1 not in set:
        # start we have start point
        # target = n+1
        # if target in set, update len and new target = target+1
        # update maxlen
        # else continue
