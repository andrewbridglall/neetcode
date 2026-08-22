class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # optimal
        # sliding window
        # init vars
        n = len(s)
        maxlen = 0
        l = r = 0
        window = defaultdict(int)
        # while window replacements <= k expand
        for r in range(n):
            window[s[r]]+=1
            maxFreq = max(window.values())
            # while len substr - maxfreq > k
            # shrink window
            while (r-l+1) - maxFreq > k:
                window[s[l]] -=1
                maxFreq = max(window.values())
                l+=1
            maxlen = max(r-l+1, maxlen)
        # return max len window
        return maxlen