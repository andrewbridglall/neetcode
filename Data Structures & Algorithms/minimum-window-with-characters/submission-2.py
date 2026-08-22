class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # optimal soln
        # init vars - countT, window dict, l,r, len
        window, countT = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] +=1
        have, need = 0, len(countT)
        start,end, reslen = -1, -1, float('inf') 
        l,r = 0, 0
        # loop
        while r < len(s):
            # add s[r] to window
            # only add c if c in countT
            if s[r] in countT:
                window[s[r]] +=1
            # update have - check if added c changes char freqs met
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have +=1
            
            # if need = have:
            while have == need:
            # check if curr len < res len
            # if true - update res len
                if r-l+1 < reslen:
                    start,end, reslen = l,r, (r-l+1)
                    print(s[start:end+1])
            # move l forward and remove s[l]
                if s[l] in countT:
                    window[s[l]] -=1
            # update have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
            
            # print(have)
            # move r forward
            r+=1
        # return res
        return s[start:end+1] if reslen != float('inf') else ''