class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len different return false
        if len(s) != len(t):
            return False
        # hashmap to store count of chars in s
        count = {}
        # iterate through s and add to map
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] +=1
        # iterate thru t and remove from map
        for c in t:
            if c not in count:
                return False
            count[c] -=1
        # if any keys not found or val nonzero = flase
        return True if max(count.values()) == 0 and min(count.values()) == 0 else False
        # else true