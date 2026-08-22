class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build edges
        # build adj from edges
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                xi,yi = points[i]
                xj,yj = points[j]
                dist = abs(xj-xi) + abs(yj-yi)
                adj[i].append([j,dist])
                adj[j].append([i,dist])
        # init vars
        visit = set()
        mst = []
        cost = 0
        minheap = []
        # choose starting point
        # point i = 0 - > node 0
        visit.add(0)
        # add edges from 0 to minheap to kick off
        for dest, weight in adj[0]:
            heapq.heappush(minheap, [weight, 0, dest])

        # while minheap
        while minheap:
            # pop curr min
            weight, src, dst = heapq.heappop(minheap)
            # edge case check - already visited
            if dst in visit:
                continue
            # process dst
            visit.add(dst)
            mst.append([src,dst])
            cost += weight
            # go to dst neighbors
            for n1,w1 in adj[dst]:
            # if visited -continue
                if n1 in visit:
                    continue
            # add negibor edge to minheap
                heapq.heappush(minheap, [w1, dst, n1])
                
        # add next smallest edge to mst
        # return cost
        return cost if len(mst) == n-1 else -1