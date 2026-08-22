class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # init vars
        n = len(s)
        minlen = n+1
        minl = minr = -1
        window = defaultdict(int)
        have = 0
        tcount = defaultdict(int)
        for c in t:
            tcount[c]+=1

        l = 0
        # iterate through s
        for r in range(n):
            # add s r to window
            char = s[r]
            window[char] +=1
            if char in tcount and window[char] == tcount[char]:
                have +=1
            # check if window valid
            # while valid - shrink
            while have == len(tcount):
                if r-l+1 < minlen:
                    minlen = r-l+1
                    minl = l
                    minr = r
                
                left_char = s[l]
                if left_char in tcount and window[left_char] == tcount[left_char]:
                    have -=1
                window[left_char] -=1
                l+=1
        
        # define helper - valid
        # return substr
        return s[minl:minr+1] if minl != -1 else ''

    def isValid(self, window, tcount):
        for key in tcount:
            if key in window and tcount[key] <= window[key]:
                continue
            else:
                return False
        return True