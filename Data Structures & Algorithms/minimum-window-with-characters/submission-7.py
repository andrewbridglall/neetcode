class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        # init vars
        n,m = len(s), len(t)
        tcount = Counter(t)
        # implement sliding window
        l = r = 0
        window = defaultdict(int)
        need, have = len(tcount), 0
        minLen, minl, minr = float('inf'), -1, -1
        while r < n:
            # add key at r to window
            rkey = s[r]
            window[rkey] += 1
            # if window key == cnt[key] - incr have 1
            if window[rkey] == tcount[rkey]:
                have +=1
            # if have == need
            while have == need:
            # store l,r if r-l+1 < currminlength else keep going
                if r-l+1 < minLen:
                    minLen = r-l+1
                    minl,minr = l,r
            # since we have all chars, try shrinking window
            # remove l
                lkey = s[l]
            # if window key at l < count[ key at l] = decr have 1
                if lkey in tcount and window[lkey] == tcount[lkey]:
                    have -=1
                window[lkey] -=1
                l+=1
            # compare have and need
            r +=1
        return s[minl:minr+1] if minl != -1 and minr != -1 else ""
                