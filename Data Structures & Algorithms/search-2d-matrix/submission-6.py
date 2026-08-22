class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init vars
        N,M = len(matrix), len(matrix[0])
        
        # binary search rows
        l, r = 0, N-1
        row = None
        while l <= r:
            m = (l+r)//2
            if target > matrix[m][0]:
                # could be row m or above
                if target <= matrix[m][M-1]:
                  row = m
                  break
                else:
                    l = m+1  
            elif target < matrix[m][0]:
                # must be before m
                r = m-1
            else:
                return True
        
        if l > r:
            return False
        # binary search within row
        l,r = 0, M-1
        while l <=r :
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        # return false default
        return False