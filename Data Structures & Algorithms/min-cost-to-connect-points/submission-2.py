class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        # compare parents
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        # compare rnaks
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # calc distances and build edges
        minheap = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                xi,yi = points[i]
                xj,yj = points[j]
                dist = abs(xj-xi) + abs(yj-yi)
                heapq.heappush(minheap, [dist, i, j])
        # run prims
        mst = []
        cost = 0
        # implement unionfind
        uf = UnionFind(n)
        # while minheap
        while minheap:
        # pop min elt
            weight, src, dst = heapq.heappop(minheap)
        # union
            if uf.union(src,dst):
                mst.append([src,dst])
                cost += weight
        

        # return min cost
        return cost