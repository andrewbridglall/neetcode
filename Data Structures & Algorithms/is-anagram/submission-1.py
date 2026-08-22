class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = sorted(s)
        s = "".join(l1)
        l2 = sorted(t)
        t = "".join(l2)
        return s == t
