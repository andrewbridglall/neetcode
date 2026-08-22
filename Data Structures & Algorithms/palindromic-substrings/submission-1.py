class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # for i in range len s
        for i in range(len(s)):
        # count odd- len palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1
                r +=1
        # count even len palindromes
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1
                r +=1
        # ret count
        return count