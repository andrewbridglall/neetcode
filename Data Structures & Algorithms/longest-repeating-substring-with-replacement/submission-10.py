class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # bf soln
        # init vars
        n = len(s)
        maxlen = 0
        maxFreq = 0
        # iter thru all substr
        for i in range(n):
            count = defaultdict(int)
            for j in range(i,n):
                count[s[j]]+=1
                maxFreq = max(count.values())
                if (j-i+1)-maxFreq <= k:
                    maxlen = max(j-i+1, maxlen)
                else:
                    break
        # create char freq
        # if n-m <= k compare to max
        # if n-m > k break and go to next start pos
        # return max length
        return maxlen