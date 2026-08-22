class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # bf soln
        # init kv store of all chars
        chars = {}
        n = len(s)
        # store start and end index of substr containing char
        for i in range(n):
            c = s[i]
        # if char already exists in kv store, already found, update end indx, then update all chars in between
            if c in chars:
                startC, _ = chars[c]
                chars[c] = [startC, i]
                for x in chars:
                    if x == c: continue
                    startX, endX = chars[x]
                    if startC <= startX and endX < i:
                        chars[x] = [startC, i]
        # else (char not found in kv store) char is new and can be added at current index i
            else:
                chars[c] = [i,i]
        # at end of str iter thru kv store and add start, end pairs to list - sort by start
        l = [item for item in chars.values()]
        l.sort()
        # then iter thru list and calc len of sub, skipping dups
        res = []
        curStart = curEnd = -1
        for start, end in l:
            if curStart == start and curEnd == end:
                continue
            curStart, curEnd = start, end
            res.append(end-start+1)
        # return list of substr
        return res