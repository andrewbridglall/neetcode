class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # run dfs
        word1_copy = word1
        def dfs(i,j, word1):
            # base case
            # i oob, j inb
            if i == len(word1) and j < len(word2):
                # insert word2[j] in word1 and call i,j
                word1 += word2[j]
                return 1 + dfs(i+1, j+1, word1)
            # i inb, j oob
            if i < len(word1) and j == len(word2):
                return 1 + dfs(i+1, j, word1)
            # i oob, j oob
            if i == len(word1) and j == len(word2):
                return 0
            # recursive case
            # word1 i == word2 j
            insert = remove = replace = len(word1)+1
            if word1[i] == word2[j]:
                return dfs(i+1,j+1, word1)
            # neq - insert, rm, repl
            else:
                # insert
                insert = 1 + dfs(i+1, j+1, word1[:i] + word2[j] + word1[i:])
                # remove
                remove = 1 + dfs(i+1, j, word1)
                # repl
                replace = 1 + dfs(i+1, j+1, word1)
            # ret min
            return min(insert, remove, replace)
        # return dfs
        return dfs(0,0, word1_copy)