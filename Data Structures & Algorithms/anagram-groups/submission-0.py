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
        p1,p2 = self.find(n1), self.find(n2)
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # calc count dict for every string in strs
        # add dicts to list of dicts
        allcounts = []
        for s in strs:
            count = defaultdict(int)
            for char in s:
                count[char] +=1
            allcounts.append(count)

        # compare all dicts
        uf = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if allcounts[i] == allcounts[j]:
                    uf.union(i,j)
        # unionfind union together dict1, dict2 if ==

        # init group by dict dict
        grouping = defaultdict(list)
        for i in range(len(strs)):
            grouping[uf.find(i)].append(strs[i])
        
        
        # for every dict:
        #   group[parent of i].append(i)

        # build res
        res = []
        for val in grouping.values():
            res.append(val)
        return res
        # for every k,v in group:
        # newlist = []
        # for index in v:
        # newlist append strs[i]
        # append newlist tores
        # return res