class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxf = 0
        maxLen = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0)+1
            maxf = max(maxf, count[s[r]])
            if r-l+1 -maxf <= k:
                maxLen = max(maxLen, r-l+1)
            else:
                count[s[l]] -=1
                l+=1
        return maxLen