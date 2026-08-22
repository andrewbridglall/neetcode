class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # init vars
        N,M = len(matrix), len(matrix[0])
        res = []
        l,r = 0, M-1
        t,b = 0, N-1
        visit = set()
        # construct while
        while l<=r and t<=b:
            # top row
            for i in range(l, r+1):
                if (t,i) in visit:
                    continue
                res.append(matrix[t][i])
                visit.add((t,i))
            # right side
            for i in range(t+1, b+1):
                if (i,r) in visit:
                    continue
                res.append(matrix[i][r])
                visit.add((i,r))
            # bottom row
            for i in range(r-1, l-1, -1):
                if (b,i) in visit:
                    continue
                res.append(matrix[b][i])
                visit.add((b,i))
            # left side
            for i in range(b-1, t, -1):
                if (i,l) in visit:
                    continue
                res.append(matrix[i][l])
                visit.add((i,l))
            # update pointers
            l +=1
            r -=1
            t +=1
            b -=1
        # return res
        return res 
