class Solution:
    def longestPalindrome(self, s: str) -> str:
        # init vars
        n = len(s)
        maxlen = 0
        maxl,maxr = 0,0
        # iterate through s
        for i in range(n):
            # odd
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    maxl,maxr = l,r
                l-=1
                r+=1
            
            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    maxl,maxr = l,r
                l-=1
                r+=1
        
        return s[maxl:maxr+1]
            