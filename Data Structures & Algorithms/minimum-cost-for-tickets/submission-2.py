class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # run dfs
        cache = {}
        n = len(days)

        def dfs(i):
            # base case
            # if i oob
            if i == len(days):
                return 0
            # update index
            # days i + 1/7/30 - end of pass
            # if end of pass < next travle day, go to next travel day stay
            # if end of pass > next travel day skip to next next
            if i in cache:
                return cache[i]
            # recursive case
            # one day pass
            onepass = costs[0] + dfs(i+1)
            # seven day pass
            k = i
            while k < n and days[k] < days[i]+7:
                k+=1
            sevenpass = costs[1] + dfs(k)
            # thrity day pass
            k = i
            while k < n and days[k] < days[i]+30:
                k+=1
            thirtypass = costs[2] + dfs(k)
            # return min
            cache[i] = min(onepass, sevenpass, thirtypass)
            return cache[i]

        # return
        return dfs(0)