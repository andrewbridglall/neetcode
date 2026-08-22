class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp soln
        # init dp array
        dp = [0]*(n+1)
        
        if not n:
            return dp
        
        dp[1] = 1
        currpwr = 1
        # iter thru nums from 0...n incl
        for num in range(2, n+1):
        # populate dp array
        # given dp i, if i == currpower * 2 - dp i = 1 and update curr power
            if num == 2 * currpwr:
                dp[num] = 1
                currpwr = num
        # else dp i = dp currpower + dp remiander
            else:
                dp[num] = dp[currpwr]+dp[num-currpwr]
        # return dp
        return dp