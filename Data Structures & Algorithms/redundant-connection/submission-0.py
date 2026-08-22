class UnionFind:
    # init
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0
    # find
    def find(self, v: int):
        p = self.par[v]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    # union
    def union(self, v1: int, v2: int):
        # find par of v1, v2
        p1, p2 = self.find(v1), self.find(v2)
        # if same ret false
        if p1 == p2:
            return False
        # compare rank
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            # equal
            self.par[p2] = p1
            self.rank[p1] +=1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # declare and init uf object
        uf = UnionFind(len(edges))
        # for every edge, union(ai, bi)
        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]
        # when union ret false return edge pair
        