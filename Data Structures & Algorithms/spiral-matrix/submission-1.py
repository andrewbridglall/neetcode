class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # init pointers
        R,C = len(matrix), len(matrix[0])
        l,r = 0, C
        t,b = 0, R
        res = []
        # while pointers valid
        while l < r and t < b:
        # append top row
            for i in range(l, r):
                res.append(matrix[t][i])
            t+=1
        # append right col
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r-=1
            if l >= r or t >= b:
                break
        # append bot row
            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            b-=1
        # append left col
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l+=1
        # update pointers
        return res