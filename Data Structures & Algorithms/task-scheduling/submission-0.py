class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # init vars
        # n = len(tasks)
        # make dict count tasks
        tmap = defaultdict(int)
        for t in tasks:
            tmap[t] +=1
        # add to maxheap
        maxheap = []
        for k,v in tmap.items():
            heapq.heappush(maxheap, [-1*v, k])
        cycle = 0
        cooldown = defaultdict(list)
        while maxheap or len(cooldown) != 0:
        # before popping from heap for cycle, add back elts that have gone thru cooldown period
            templist = cooldown.pop(cycle, [])
            for item in templist:
                heapq.heappush(maxheap, item)
        # heappop max from heap
            if maxheap:
                count, task = heapq.heappop(maxheap)
        # decrement count - being used for current cycle
        # add <count, max> to cooldown map at cycle + n + 1 - becomes available here
                if count+1 < 0:
                    cooldown[cycle+n+1].append([count+1, task])
        # increment cycle - equals next cycle
            cycle +=1
        # cycle at end will be 1 more than last cycle zero indexed - will be cardinality of cycles
        # hence return cycles
        return cycle
