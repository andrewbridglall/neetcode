class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # build count hashmap
        count = defaultdict(int)
        for num in nums:
            count[num] +=1
        # init res
        res = []
        # build dfs
        def dfs(currset, count):
            # base case
            if len(currset) == len(nums):
                res.append(currset.copy())
                return
            # recursive case
            for key in count:
                if count[key] > 0:
                    currset.append(key)
                    count[key] -=1
                    dfs(currset, count)
                    
                    currset.pop()
                    count[key] +=1
        # run dfs
        dfs([], count)
        # ret res
        return res