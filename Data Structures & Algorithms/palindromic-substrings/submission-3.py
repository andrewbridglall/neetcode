class Solution:
    def countSubstrings(self, s: str) -> int:
        # bf
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                length = j-i+1
                # if odd len
                if length % 2:
                    l = r = (i+j)//2
                    while l >= i and r <= j and s[l] == s[r]:
                        l -=1
                        r +=1
                    if l == i-1 and r == j+1:
                        count +=1
                # even len
                else:
                    l, r = (i+j)//2, (i+j)//2 +1
                    while l >= i and r <= j and s[l] == s[r]:
                        l -=1
                        r +=1
                    if l == i-1 and r == j+1:
                        count +=1
        return count