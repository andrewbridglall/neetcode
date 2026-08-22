class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLen = 0
        count = {}
        for r in range(len(s)):
            # add char to char count map
            count[s[r]] = count.get(s[r], 0)+1
            # get most freq
            maxfreq = 0
            for val in count.values():
                maxfreq = max(maxfreq, val)
            # if len - most freq char count <= k: update maxLen
            if (r-l+1) - maxfreq <= k:
                maxLen = max(maxLen, r-l+1)
            else:
                count[s[l]] -=1
                l +=1
            # else move l up and remove s[l]
        return maxLen    
        