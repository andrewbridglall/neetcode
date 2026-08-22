class Solution:
    def longestPalindrome(self, s: str) -> str:
        gmax_l, gmax_r = 0,0
        for i in range(len(s)):
            max_l, max_r = 0,0
            # odd len palin
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_r - max_l +1:
                    max_l, max_r = l,r
                l -=1
                r +=1
            # even len palin
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_r - max_l +1:
                    max_l, max_r = l,r
                l -=1
                r +=1
            if max_r-max_l+1 > gmax_r-gmax_l+1:
                gmax_l,gmax_r = max_l,max_r
        return s[gmax_l:gmax_r+1]
            
        