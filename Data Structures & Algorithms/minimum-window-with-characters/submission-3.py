class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # bf - build all substr and check each
        # init vars
        n = len(s)
        minlen = len(s)+1
        minl,minr = -1, -1
        countT = defaultdict(int)
        for k in range(len(t)):
            countT[t[k]]+=1
        # iterate through s
        for i in range(n):
            for j in range(i,n):
                # substr i to j
                countS = defaultdict(int)
                for k in range(i,j+1):
                    countS[s[k]]+=1
                valid = True
                for key in countT:
                    if key in countS and countT[key] <= countS[key]:
                        continue
                    else:
                        valid = False
                        break
                if valid and j-i+1 < minlen:
                        minl,minr = i,j
                        minlen = j-i+1
        # return min len substr else empty str
        return s[minl:minr+1] if minlen < len(s)+1 else ""