class Solution:
    def climbStairs(self, n: int) -> int:
        #make iterative soln runs in n time
        #no recursive stack - o1 space
        
        # if n ==1 or 2 return n
        if n < 3:
            return n

        # init vars
        prev2 = 1 # n=1
        prev1 = 2 # n=2
        res = 0

        for _ in range(n-2):
            res = prev1 + prev2

            prev2 = prev1
            prev1 = res
        
        return res
        # start with init vals
        # iterate n times updating vals
        # finally return res