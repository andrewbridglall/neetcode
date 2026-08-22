class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init vars
        maxlen = 0
        n = len(s)
        l = 0
        count = defaultdict(int)
        
        # iter thru s - sldiing window
        for r in range(n):

            # add to substr
            count[s[r]] +=1
            maxfreq = max(count.values())
            repl = (r-l+1) - maxfreq

            # if replacements <=k: update maxlen and proceed
            if repl <=k:
                maxlen = max(maxlen, r-l+1)
            # else replace > k: remove s[l], update replacement
            while repl > k:
                count[s[l]] -=1
                l+=1
                maxfreq = max(count.values())
                repl = (r-l+1)-maxfreq
        return maxlen
