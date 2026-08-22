class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # calc weights and build adj list
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # building edge between i and j, j and i
                # calc weight given formula
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                weight = abs(xi-xj) + abs(yi-yj)
                # append to adj list
                adj[i].append([j, weight])
                adj[j].append([i, weight])
        
        # prims
        visit = set()
        minheap = []
        mst = []
        cost = 0

        # init visit and minheap
        visit.add(0)
        for d, w in adj[0]:
            heapq.heappush(minheap, [w, 0, d])

        while minheap:
            # pop min from heap
            weight, src, dst = heapq.heappop(minheap)
            # if dst already visited skip
            if dst in visit:
                continue
            # add to visit
            # add edge to mst
            # add wegiht to cost
            visit.add(dst)
            mst.append([src, dst])
            cost += weight
            # add neighors of dst
            # if neighbor already in visit skip
            for node, w1 in adj[dst]:
                if node in visit:
                    continue
                heapq.heappush(minheap, [w1, dst, node])

        
        return cost if len(mst) == len(points)-1 else -1