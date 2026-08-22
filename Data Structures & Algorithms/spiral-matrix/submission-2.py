class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # bf - extra space - lazy way
        # init vars
        m,n = len(matrix), len(matrix[0])
        res = []
        visit = set()
        l = 0
        r = n-1
        t = 0
        b = m-1
        # iter thru matrix layer by layer - while valid
        while t <= b and l <= r:
        # at each layer make 4 distinct operations
            # top row
            for col in range(l, r+1):
                if (t,col) in visit:
                    continue
                res.append(matrix[t][col])
                visit.add((t,col))
            # right col
            for row in range(t, b+1):
                if (row,r) in visit:
                    continue
                res.append(matrix[row][r])
                visit.add((row,r))
            # bot row
            for col in range(r, l-1, -1):
                if (b,col) in visit:
                    continue
                res.append(matrix[b][col])
                visit.add((b,col))
            # left col
            for row in range(b, t-1, -1):
                if (row, l) in visit:
                    continue
                res.append(matrix[row][l])
                visit.add((row, l))
            
            # update ptrs
            l +=1
            r -=1
            t +=1
            b -=1
        # handle edge cases to avoid duplicate entries
        return res