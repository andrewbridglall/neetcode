class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adj list
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for s,d,t in times:
            adj[s].append([d,t])
        # declare data structs - hashmap, minheap
        sp = {}
        minheap = []
        # init - add src edges to minheap
        minheap.append([0, k, k])
        # while minheap
        while minheap:
        # pop from minheap => weight, src, dst
            time, src, dst = heapq.heappop(minheap)
        # if dst in map: continue
            if dst in sp:
                continue
        # add dst to map with weight
            sp[dst] = time
        # for neighbor in adj[dst] add weight+w1, dst, neighbor to minheap
            for n1, t1 in adj[dst]:
                heapq.heappush(minheap, [time+t1, dst, n1])
        # repeat until minheap empty
        # return max of map if len = n else -1
        # print(sp)
        return max(sp.values()) if len(sp) == n else -1