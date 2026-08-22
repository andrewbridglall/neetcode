class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursive approach
        cache = {}
        def pow(x, n):
            # base case
            # if n = 0
            if n == 0:
                return 1
            # if n == 1 
            if n == 1:
                return x
            if (x,n) in cache:
                return cache[(x,n)]
            # recursive case
            # if n < 0
            if n < 0:
                return 1/pow(x, abs(n))
            # n even
            cache[(x,n)] = pow(x, n//2)*pow(x, n//2)
            # n odd
            if n % 2 == 1:
                cache[(x,n)] *= x
            return cache[(x,n)]
        return pow(x,n)