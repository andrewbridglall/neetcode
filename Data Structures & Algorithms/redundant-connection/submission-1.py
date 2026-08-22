class UnionFind:

    def __init__(self,n):
        # from 1... n
        self.par = {}
        self.rank = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 1
        
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1,n2):
        # compare parents
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        # compare ranks
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # implement unionfind
        n = len(edges)
        uf = UnionFind(n)
        # build graph one edge at time starting at beginnning
        # if cycle detected while adding edge, return that edge
        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]
        return -1
