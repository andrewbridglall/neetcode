class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # bf
        # substr len
        mindata = (float('inf'), -1, -1)
        # init t dict count
        count_t = defaultdict(int)
        for c in t:
            count_t[c] +=1
        # get all substr
        for i in range(len(s)):
            for j in range(i, len(s)):
                valid = True
                temp = defaultdict(int)
                for k in range(i, j+1):
                    temp[s[k]] +=1
                for c in count_t:
                    if count_t[c] > temp[c]:
                        valid = False
                        break
                if  valid and j-i+1 < mindata[0]:
                    mindata = (j-i+1, i, j)
        # for each substr get coutns
        # check all chars and freq in t match subst
        # if true -> compare to min
        # else continue
        # return min substr if valid else empty string
        minlen, l, r = mindata
        return s[l:r+1] if minlen != float('inf') else ''