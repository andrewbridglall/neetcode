class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # bf soln
        # edge case check
        n = len(s)
        m = len(t)
        if n < m:
            return ""
        tcnt = defaultdict(int)
        for c in t:
            tcnt[c] +=1
        need = len(tcnt)
        minLen, minL, minR = float('inf'), -1, -1
        # calc all substr of s
        for i in range(n):
            have = 0
            window = defaultdict(int)
            for j in range(i,n):
                # add char j to have if in t
                key = s[j]
                if key not in tcnt:
                    continue
                window[key] +=1
                if window[key] == tcnt[key]:
                    have +=1
                if have == need:
                    if j-i+1 < minLen:
                        minLen = j-i+1
                        minL,minR = i,j
        return s[minL:minR+1] if minL != -1 and minR != -1 else ""
        
        # count chars in substr
        # if have == need update minlength and store i,j
        # return substr if valid else empty str