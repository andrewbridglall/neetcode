class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = { n: True for n in nums}
        currLen, maxLen = 0, 0
        for n in nums:
            currnum = n
            while currnum in numMap:
                currLen +=1
                currnum +=1
            maxLen = max(maxLen, currLen)
            currLen = 0
        return maxLen


