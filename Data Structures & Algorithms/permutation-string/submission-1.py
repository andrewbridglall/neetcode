class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        n,m = len(s1), len(s2)
        if m < n:
            return False
        # add letters in s1 to hashmap
        letters = defaultdict(int)
        for s in s1:
            letters[s] += 1
        # iterate thru s2 and check if all letters found consecutively
        m = len(s2)
        for i in range(m):
        # make copy of map
            if i+n > m:
                break
            letterCopy = letters.copy()
            for j in range(i, i+n):
                if s2[j] not in letterCopy:
                    break
                elif letterCopy[s2[j]] == 0:
                    break
                
                letterCopy[s2[j]] -=1
            if max(letterCopy.values()) == 0:
                return True
        return False