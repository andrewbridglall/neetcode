class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(i):
            if i == len(nums):
                return [[]]
            perms = permutation(i+1)
            newPerms = []
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    newPerms.append(pCopy)
            return newPerms
        
        return permutation(0)