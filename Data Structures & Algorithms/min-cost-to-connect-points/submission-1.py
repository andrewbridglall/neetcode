class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1,n2):
        # p1,p2 = find n1,n2
        p1, p2 = self.find(n1), self.find(n2)
        # if p1 eq p2 - return false -same connected component
        if p1 == p2:
            return False
        # if rank p2 < rank p1 - set p1 to be parent of p2
        if self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        # elif rank p1 < rank p2 - p2 is parent p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        # else equal - set p1 as par and incr rank p1
        else:
            self.par[p2] = p1
            self.rank[p1] +=1
        # return true
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # implement with kruskal's algorithm
        # build uf class
        
        # build list edges with weights
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i][0], points[i][1] 
                xj, yj = points[j][0], points[j][1]
                w = abs(xi-xj) + abs(yi-yj)
                edges.append([i, j, w])        
        
        # declare uf with n = len points
        # declare minheap, mst, cost
        minheap = []
        mst = []
        cost = 0
        uf = UnionFind(len(points))

        # push all edges to minheap
        for s,d,w in edges:
            heapq.heappush(minheap, [w,s,d])
        # while minheap
        while minheap:
        # pop from minheap
            w,n1,n2 = heapq.heappop(minheap)
        # if union n1,n2 true - append to mst, sum weight to cost
            if uf.union(n1,n2):
                mst.append([n1,n2])
                cost += w

        # return cost if len mst == n-1 else -1
        return cost if len(mst) == len(points)-1 else -1