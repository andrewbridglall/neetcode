class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init vars
        maxlen = 0
        n = len(s)
        # iterate through all substr
        for i in range(n):
            for j in range(i,n):
                # substr i to j
                count = defaultdict(int)
                for c in range(i,j+1):
                    count[s[c]]+=1
                maxfreq = max(count.values())
                repl = (j-i+1)-maxfreq
                if repl <= k:
                    maxlen = max(maxlen, j-i+1)
        # if replacements <= k - try ot update maxlen
        # return maxlen
        return maxlen