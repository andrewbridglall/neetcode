class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bf
        # keep track of max
        n = len(s)
        maxlen = 0
        lmax, rmax = 0,0
        # find all substr
        for i in range(n):
            for j in range(i, n):
                # substr i...j
                # check if substr is palindrome
                l,r = i,j
                isPalindrome = True
                while l <= r:
                    if s[l] != s[r]:
                        isPalindrome = False
                        break
                    l +=1
                    r -=1
                if isPalindrome and j-i+1 > maxlen:
                    maxlen = max(maxlen, j-i+1)
                    lmax,rmax = i,j

        # return max
        return s[lmax:rmax+1]