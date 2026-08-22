class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        n = len(s)
        maxLen = -1

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                maxLen = max(maxLen, j-i+1)
        return 0 if maxLen == -1 else maxLen