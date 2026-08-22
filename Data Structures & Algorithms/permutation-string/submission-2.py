class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init vars and data struct
        n,m = len(s1), len(s2)
        # store count of chars in s1
        count = defaultdict(int)
        for s in s1:
            count[s] +=1
        print(count)
        # define sliding window of len s1
        window = defaultdict(int)
        l = 0
        for r in range(m):
            # if size exceeds n remove char at l and incr l
            if r-l+1 > n:
                window[s2[l]] -=1
                if not window[s2[l]]:
                    del window[s2[l]]
                l +=1
            # add s2 r to window count
            window[s2[r]] +=1
            # check if window count matches s1 count
            print(window)
            if count == window:
                return True
        # iter thru s2 and keep count of chars in window
        # if window freq match count of chars in s1 - ret true
        # else false
        return False