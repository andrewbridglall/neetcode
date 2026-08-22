class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # recursive soln
        # init vars
        # pad nums with 1s
        nums = [1] + nums + [1]
        n = len(nums)
        cache = defaultdict(int)
        # make dfs
        def dfs(l,r):
            # base case
            if (l,r) in cache:
                return cache[(l,r)]
            # recursive case
            maxcoins = 0
            # choose k
            for k in range(l+1, r):
            # calc coins and then go to dfs l k and dfs k r
                coins = nums[l]*nums[k]*nums[r] + dfs(l,k) + dfs(k,r)
                maxcoins = max(maxcoins, coins)
            # ret max coins
            cache[(l,r)] = maxcoins
            return maxcoins
        # run dfs
        # return maxcoins
        return dfs(0, n-1)