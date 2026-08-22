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
    
    def union(self, n1,n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected acyclic graph
        # implement union find
        uf = UnionFind(n)
        # union edge nodes
        # if false = cycle detected return false
        # else return true if rank of parent == n
        for n1,n2 in edges:
            if not uf.union(n1,n2):
                return False

        p1 = uf.find(0)
        return uf.rank[p1] == n
