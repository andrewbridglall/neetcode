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
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # init uf object
        uf = UnionFind(len(accounts))
        # map email -> account
        # union accounts
        emailToAcct = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in emailToAcct:
                    uf.union(emailToAcct[email], i)
                else:
                    emailToAcct[email] = i
        # map acct parent to email lists
        emailParents = defaultdict(set)
        for i in range(len(accounts)):
            # get parent of account i
            par = uf.find(i)
            for email in accounts[i][1:]:
               emailParents[par].add(email)
                
            # append emails from account i to parent
        
        res = []
        for index, emails in emailParents.items():
            res.append([accounts[index][0]] + sorted(list(emails)))
        return res