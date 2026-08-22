class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        countS, countT = {}, {}
        for i in range(len(s)):
            if s[i] not in countS:
                countS[s[i]] = 0
            countS[s[i]] +=1
            
            if t[i] not in countT:
                countT[t[i]] = 0
            countT[t[i]] +=1
        return countS == countT