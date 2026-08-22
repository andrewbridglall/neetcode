class UnionFind:
    def __init__(self, n : int):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        self.numComponents = n
    # find
    def find(self, v: int):
        p = self.par[v]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    # union
    def union(self, v1: int, v2: int):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] +=1
        self.numComponents -=1
        return True
    # add in numcomponents

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        return uf.numComponents