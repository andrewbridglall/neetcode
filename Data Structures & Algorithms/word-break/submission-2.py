class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # make dfs soln
        # memo
        cache = {}
        # at pos i in string s, word j in worddict
        def dfs(i,j):
            # base case
            # if no match found -ret False
            if i == len(s):
                return True            
            m = len(wordDict[j])
            if s[i:i+m] != wordDict[j]:
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            # if i == len s - reached end - ret True
            # recursive case
            # try all words j at pos i
            # if here, means worddict j was match
            # update i and make recurisve call
            match = False
            for k in range(len(wordDict)):
                match |= dfs(i+m, k)
            cache[(i,j)] = match
            return cache[(i,j)]
        
        for k in range(len(wordDict)):
                if dfs(0, k):
                    return True
        return False