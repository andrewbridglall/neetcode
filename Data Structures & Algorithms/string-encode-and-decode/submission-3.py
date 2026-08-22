class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        while i < len(s):
            digits = ""
            while s[i] != '#':
                digits += s[i]
                i+=1
            res.append(s[i+1:i+1+int(digits)])
            i = i+1+int(digits)
        return res
        