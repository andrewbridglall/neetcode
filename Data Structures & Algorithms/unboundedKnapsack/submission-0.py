class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # two branch recursion -brute force
        # include 1 more, skip

        # build dfs
        def dfs(i, cap):
            # base case
            # if i oob -no more incremental profit
            if i == len(profit):
                return 0
            # recursive case
            # skip i
            skip = dfs(i+1, cap)
            # include 1 more occurrence of i
            include = 0
            if cap-weight[i] >=0:
                include = profit[i] + dfs(i, cap-weight[i])
            # return max of include skip 
            return max(skip, include)

        # run dfs
        return dfs(0, capacity)

