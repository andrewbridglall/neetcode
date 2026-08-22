class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # bf - recursive and check if perm already exists
        # build dfs
        # strategy - go to end of arr, return empty list
        # as backtrack, add nums of i to every perm in list until add 0
        # return dfs
        def dfs(i):
            # base case
            if i == len(nums):
                return [[]]
            perms = dfs(i+1)
            # recursive case
            newperms = []
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    if pCopy not in newperms:
                        newperms.append(pCopy)
            return newperms

        # run dfs
        return dfs(0)