class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,1]
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        base = 2
        for num in range(3, n+1):
            # if num is power of 2, update base
            if num == 2*base:
                base = 2*base
                dp[num] = 1 
                continue
            dp[num] = dp[num-base]+dp[base]
        return dp
