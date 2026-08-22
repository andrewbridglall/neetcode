class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bf
        n = len(s)
        maxlen = 0
        maxl,maxr = 0,0
        # calc all substr
        # determine if substr palindrome
        def isPalindrome(s):
            l,r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        for i in range(n):
            for j in range(i,n):
                # substr from i...j
                if isPalindrome(s[i:j+1]) and j-i+1 > maxlen:
                    maxlen = j-i+1
                    maxl,maxr = i,j
        # return longest
        return s[maxl:maxr+1]

