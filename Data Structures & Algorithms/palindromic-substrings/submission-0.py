class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # iterate through str s
        for i in range(len(s)):
        # check for palindromes of odd len
            l = r = i
            while l >=0 and r < len(s) and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
        # check for palindromes of even len
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
        # every time palindrome detected, incr count by 1
        # return count
        return count