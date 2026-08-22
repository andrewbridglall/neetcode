class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # make dfs
        # run dfs
        cache = {}
        def dfs(i):
            # base case
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            # recursive case
            # iterate through all words
            # check if equivalent to substr starting at i
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        return True
            cache[i] = False
            return cache[i]
        
        return dfs(0)