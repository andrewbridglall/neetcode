class Solution:
    def longestPalindrome(self, s: str) -> str:
        # keep track of max
        maxlen, maxl, maxr = 0,0,0
        # iterate through str
        for i in range(len(s)):
        # try odd len palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    maxl, maxr = l,r
                l -=1
                r +=1
        # try even len palindrome
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    maxl, maxr = l,r
                l -=1
                r +=1
        # return substring
        return s[maxl:maxr+1]