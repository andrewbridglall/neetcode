class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        # if sum nums odd - cant split in half - ret false
        if n % 2: return False

        target = n // 2
        
        # build dfs - keep track of sum, target = n/2
        def dfs(i, tar):
            # base case
            # if summ == targ wrd
            if tar == 0:
                return True
            # if i oob return
            if i == len(nums):
                return False
            # recursive case
            # include item i
            # skip item i
            return dfs(i+1, tar-nums[i]) or dfs(i+1, tar) 
        
        
        # run dfs
        # return
        return dfs(0, target)