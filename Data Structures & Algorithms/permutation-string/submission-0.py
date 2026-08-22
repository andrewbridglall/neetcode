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
            substr_map = defaultdict(int)
            for j in range(i, i+n):
                if s2[j] not in letters:
                    break
                substr_map[s2[j]] +=1
            if letters == substr_map:
                return True
        return False