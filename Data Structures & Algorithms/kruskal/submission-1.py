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
        # if p1 eq p2 return false
        if p1 == p2:
            return False
        # if rank p1 < rank p2 - set parent of p1 = p2
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        # elif rank p2 < rank p1 - set parent of p2 = p1
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        # else - rank ==, set parent p2 = p1 and rank p1 ++
        else:
            self.par[p2] = p1
            self.rank[p1] +=1
        # return true
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # approach - get min edge not part of connected component
        # declare and build unionfind class
        # declare minheap, unionfind object with n nodes 0 indexed
        minheap = []
        uf = UnionFind(n)
        mst = []
        cost = 0
        # add all edges to minheap
        for s,d,w in edges:
            heapq.heappush(minheap, [w,s,d])
        # while minheap
        while minheap:
        # pop from minheap
            w,n1,n2 = heapq.heappop(minheap)
        # if union n1 n2 is true - add to mst, add weight to cost
            if uf.union(n1,n2):
                mst.append([n1,n2])
                cost += w
        # if union if false - nodes already part of connected compoennt =continue
        # if len mst is n-1 return cost else -1 
        return cost if len(mst) == n-1 else -1
