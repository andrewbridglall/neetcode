class UF:
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
    
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] +=1
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # declare unionfind class
        uf = UF(len(nums))
        # map num -> index
        numMap = {}
        for i, num in enumerate(nums):
            numMap[num] = i
        # if consecutive int found in nums: union
        for num, index in numMap.items():
            if num+1 in numMap:
                uf.union(index, numMap[num+1])    
        # map par -> count
        parMap = defaultdict(int)
        for i in range(len(nums)):
            p = uf.find(i)
            parMap[p] +=1
        
        # return max count
        return max(parMap.values())