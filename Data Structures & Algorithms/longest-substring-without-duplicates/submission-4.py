class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init vars
        l = 0
        maxlen = 0
        charSet = set()
        # iterate through s
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            maxlen = max(maxlen, r-l+1)
        # return len
        return maxlen