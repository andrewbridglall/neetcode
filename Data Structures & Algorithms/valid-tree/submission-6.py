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
        # get parents
        p1,p2 = self.find(n1), self.find(n2)
        # if parents eq - false
        if p1 == p2:
            return False
        # compare rank and ret true
        if self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # implement unionfind
        uf = UnionFind(n)
        # iterate through edges
        # union n1,n2
        # if false - cycle detected - return
        for a,b in edges:
            if not uf.union(a,b):
                return False
        # return size of connected componenet == n
        return uf.rank[uf.find(0)] == n