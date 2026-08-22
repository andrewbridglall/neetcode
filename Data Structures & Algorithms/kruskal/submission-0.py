class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        # p1, p2 = find n1 n2
        p1, p2 = self.find(n1), self.find(n2)
        # if p1 eq p2 ret false
        if p1 == p2:
            return False
        # if rank p1 < rank p2 
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        # if rank p2 < rank p1
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        # else =
        else:
            self.rank[p1] +=1
            self.par[p2] = p1
        # ret true
        return True
    
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # declare and init uf, minheap, mst
        uf = UnionFind(n)
        minHeap = []
        mst = []
        total = 0
        # add all edges to minheap
        for s, d, w in edges:
            heapq.heappush(minHeap, [w, s, d])
        # while minheap
        while minHeap:
            # pop from minheap -> w, n1, n2
            w, s, d = heapq.heappop(minHeap)
            # union n1, n2
            # if union == true append to mst and update weight
            if uf.union(s,d):
                mst.append([s,d])
                total += w
        # return weight if valid mst else -1
        return total if len(mst) == n-1 else -1