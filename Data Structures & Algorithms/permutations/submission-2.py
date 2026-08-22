class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        currPerms, newPerms = [[]], []
        for i in range(len(nums)):
            for p in currPerms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    newPerms.append(pCopy)
            currPerms = newPerms
            newPerms = []
        return currPerms