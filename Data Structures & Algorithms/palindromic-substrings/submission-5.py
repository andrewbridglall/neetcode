class Solution:
    def countSubstrings(self, s: str) -> int:
        # init vars
        n = len(s)
        count = 0
        # iterate through s
        for i in range(n):
        # build palindromes starting at i
            # odd
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
            
            # even
            l,r = i,i+1
            while l >= 0 and r < n and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
        # return count
        return count