class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # build adj list
        adj = {}
        for i in range(n):
            adj[i] = []
        for s,d,w in edges:
            adj[s].append([d,w])
            adj[d].append([s,w])
        
        # init mst, minheap, visit
        # add src to visit, push src edges to heap
        mst, minheap, visit, total = [], [], set(), 0
        visit.add(0)
        for d, w in adj[0]:
            heapq.heappush(minheap, [w, 0, d])
            
        # while minheap
        while minheap:
            # pop from heap => w, src, dst
            w, src, dst = heapq.heappop(minheap)
            # if dst in visit - skip
            if dst in visit:
                continue
            # add to visit
            # add src dst to mst
            visit.add(dst)
            mst.append([src, dst])
            total += w
            # for neighbors of dst
            # push neighbor edges to minheap
            # if neighbor already visited - skip
            for neighbor, weight in adj[dst]:
                if neighbor in visit:
                    continue
                heapq.heappush(minheap, [weight, dst, neighbor])
        # return mst/total weight
        return -1 if len(mst) != n-1 else total