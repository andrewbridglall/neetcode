class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s to lower
        s = s.lower()
        n = len(s)
        # init l,r
        l,r = 0, n-1 
        # while l < r
        while l < r:
        # if s of l or s of r non alpha = skip
            if not s[l].isalnum():
                l +=1
            elif not s[r].isalnum():
                r -=1
        # elif are alpha but s l != s r = ret false
            elif s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        # else - s l and s r are alpha and == = update l r

        # ret true by default
        return True