class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # init vars
        # make dfs
        def dfs(i):
            # base case
            # if i oob return empty set perms
            if i == len(nums):
                return [[]]
            # recursive case
            # perms = dfs i+1
            perms = dfs(i+1)
            # iterate thru all p in perms
            newperms = []
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    newperms.append(pCopy)
            # at every pos in p, insert nums i
            # append to newperms
            # return newperms
            return newperms
        # run dfs
        # dfs 0 will returan all perms
        # return res
        return dfs(0)