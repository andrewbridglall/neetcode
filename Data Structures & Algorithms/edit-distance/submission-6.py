class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # run dfs
        cache = {}

        def dfs(i,j):
            # base case
            # if j oob
            if j == len(word2):
                return len(word1[i:])
            # if i oob
            if i == len(word1):
                return len(word2[j:])
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # if word1 i == word2 j
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            # if neq - insert, remove repl
            else:
                # insert
                insert = 1 + dfs(i, j+1)
                # remove
                remove = 1 + dfs(i+1, j)
                # replace
                replace = 1 + dfs(i+1, j+1)

                cache[(i,j)] = min(insert, remove, replace)
                return cache[(i,j)]
            # return min(insert, rm , repl)

        # return dfs
        return dfs(0,0)
