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
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] +=1
        return True
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # define uf
        # build mst, calc cost of original mst
        minheap = []
        mst = []
        cost = 0
        uf = UnionFind(n)
        # add all edges to minheap
        for s,d,w in edges:
            heapq.heappush(minheap, [w, s, d])
        
        # while minheap
        while minheap:
        # pop from minheap
            w, n1,n2 = heapq.heappop(minheap)
            if uf.union(n1,n2):
                mst.append([n1,n2])
                cost += w
        # connect unconnected nodes
        # add to mst
        # add to cost
        
        # find critical edges
        critical = []
        pseudo = []
        # for every edge, skip each and recalc mst cost - if newcost > original: edge is critical
        for i in range(len(edges)):
            minheap = []
            newmst = []
            newcost = 0
            uf = UnionFind(n)
            # add all edges to minheap
            for j in range(len(edges)):
                if j == i:
                    continue
                s,d,w = edges[j][0], edges[j][1], edges[j][2] 
                heapq.heappush(minheap, [w, s, d])
            
            # while minheap
            while minheap:
            # pop from minheap
                w, n1,n2 = heapq.heappop(minheap)
                if uf.union(n1,n2):
                    newmst.append([n1,n2])
                    newcost += w
            if newcost > cost or len(newmst) != n-1:
                critical.append(i)
                continue
        # **find pseudocritical - in some not all - new mst cost = old mst cost
        # force edge into mst then build - if cost == original cost and mst valid - then append to pseudo
            minheap = []
            newmst = []
            newcost = 0
            uf = UnionFind(n)
            
            s,d,w = edges[i][0], edges[i][1], edges[i][2]
            newmst.append([s,d])
            newcost += w
            uf.union(s,d)

            # add all edges to minheap
            for j in range(len(edges)):
                s,d,w = edges[j][0], edges[j][1], edges[j][2] 
                heapq.heappush(minheap, [w, s, d])
            
            # while minheap
            while minheap:
            # pop from minheap
                w, n1,n2 = heapq.heappop(minheap)
                if uf.union(n1,n2):
                    newmst.append([n1,n2])
                    newcost += w
            print(newmst)
            if newcost == cost and len(newmst) == n-1:
                pseudo.append(i)
        
        return [critical, pseudo]

