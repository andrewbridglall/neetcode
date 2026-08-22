class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        # store data in arr len n+1 s.t. index = n
        arr = [-1]*(n+1)

        #init base cases, skipping arr[0]
        arr[1], arr[2] = 1,2

        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return arr[n]