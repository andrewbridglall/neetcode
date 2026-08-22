class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [0]*(2)

        for i in range(len(s)):
            dp[1] = 0
            # check for palindrome - odd
            odd_l,odd_r = i,i
            oddlen = 0
            while odd_l >= 0 and odd_r < n and s[odd_l] == s[odd_r]:
                oddlen = odd_r-odd_l+1
                odd_l -=1
                odd_r +=1
            # check for palindrome - even
            even_l,even_r = i, i+1
            evenlen = 0
            while even_l >= 0 and even_r < n and s[even_l] == s[even_r]:
                evenlen = even_r-even_l+1
                even_l -=1
                even_r +=1
            dp[1] = (odd_l+1, odd_r-1) if oddlen > evenlen else (even_l+1, even_r-1)
            # compare to dp i-1 if i-1 in bound
            # store max len
            if i-1 >= 0:
                prev_l, prev_r = dp[0]
                curr_l, curr_r = dp[1]
                
                dp[1] = dp[0] if prev_r-prev_l+1 > curr_r-curr_l+1 else dp[1]
            dp[0] = dp[1]
        # return dp -1
        l, r = dp[0]
        return s[l:r+1]

