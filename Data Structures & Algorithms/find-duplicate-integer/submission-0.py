class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count[n]+1 if n in count else 1
            if count[n] > 1:
                return n
