class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # separate into two 'piles'
        dp = {}
        amount = math.ceil(sum(stones)/2)
        # 2 branch recursion
        # return total closest to total
        # make dfs
        def dfs(i, total):
            # base case
            if i == len(stones):
                return total
            if (i, total) in dp:
                return dp[(i, total)]
            # recursive case
            # include i
            include = 0
            if total+stones[i] <= amount:
                include = dfs(i+1, total+stones[i])
            # skip i
            skip = dfs(i+1, total)
            # return max include skip
            dp[(i,total)] = max(include, skip) 
            return dp[(i,total)]


        # dfs returns total
        tot = dfs(0,0)
        # return (sum-total) -total
        return abs(tot - (sum(stones)-tot))