class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # run dfs
        cache = {}

        def dfs(i, lastDay):
            # base case
            # if i oob
            if i == len(days):
                return 0
            # update index
            # days i + 1/7/30 - end of pass
            # if end of pass < next travle day, go to next travel day stay
            # if end of pass > next travel day skip to next next
            if lastDay > days[i]:
                return dfs(i+1, lastDay)
            if (i, lastDay) in cache:
                return cache[(i,lastDay)]
            # recursive case
            # one day pass
            onepass = costs[0] + dfs(i+1, days[i]+1)
            # seven day pass
            sevenpass = costs[1] + dfs(i+1, days[i]+7)
            # thrity day pass
            thirtypass = costs[2] + dfs(i+1, days[i]+30)
            # return min
            cache[(i,lastDay)] = min(onepass, sevenpass, thirtypass)
            return cache[(i,lastDay)]

        # return
        return dfs(0,0)