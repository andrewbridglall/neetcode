class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # init vars
        n = len(s)
        minlen = n+1
        minl = minr = -1
        window = defaultdict(int)
        
        tcount = defaultdict(int)
        for c in t:
            tcount[c]+=1

        l = 0
        # iterate through s
        for r in range(n):
            # add s r to window
            window[s[r]] +=1
            # check if window valid
            # while valid - shrink
            while self.isValid(window, tcount):
                if r-l+1 < minlen:
                    minlen = r-l+1
                    minl = l
                    minr = r
                window[s[l]] -=1
                l+=1
        
        # define helper - valid
        # return substr
        return s[minl:minr+1] if minlen < n+1 else ''
        
    def isValid(self, window, tcount):
        for key in tcount:
            if key in window and tcount[key] <= window[key]:
                continue
            else:
                return False
        return True