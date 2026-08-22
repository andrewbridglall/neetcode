class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # optimal - no extra space
        # init vars
        m,n = len(matrix), len(matrix[0])
        res = []
        l = 0
        r = n-1
        t = 0
        b = m-1
        # iter thru matrix layer by layer - while valid
        while t <= b and l <= r:
        # at each layer make 4 distinct operations
            # top row
            for col in range(l, r+1):
                res.append(matrix[t][col])
            t +=1
            # right col
            for row in range(t, b+1):
                res.append(matrix[row][r])
            r -=1

            if t > b or l > r:
                break

            # bot row
            for col in range(r, l-1, -1):
                res.append(matrix[b][col])
            b -=1

            # left col
            for row in range(b, t-1, -1):
                res.append(matrix[row][l])
            l +=1

        return res