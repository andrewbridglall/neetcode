class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adj list
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for s,d,w in times:
            adj[s].append([d,w])
        # init vars
        # minheap, shortest
        shortest = defaultdict(int)
        minheap = []
        # run dijkstras
        minheap.append([0,k,k])
        while minheap:
            # w, s, d = pop from minheap
            w, s, d = heapq.heappop(minheap)
            # add path to shortest
            if d in shortest:
                continue
            shortest[d] = w
            # iterte thru neighbors of d
            # if neighbors already in shortest - skip
            # add neighbors with cumulative weight to reach it
            for n1, w1 in adj[d]:
                if n1 in shortest:
                    continue
                heapq.heappush(minheap, [w+w1, d, n1])

        # get shortest map and process
        return max(shortest.values()) if len(shortest) == n else -1