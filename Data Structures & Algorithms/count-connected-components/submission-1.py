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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # implement unionfind
        uf = UnionFind(n)
        # given edges, union a b
        for a,b in edges:
            uf.union(a,b)
        # init count
        components = set()
        # count freq parents
        for i in range(n):
            components.add(uf.find(i))
        # return len count map
        return len(components)