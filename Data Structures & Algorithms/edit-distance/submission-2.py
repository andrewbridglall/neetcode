class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # run dfs
        # word1_copy = word1

        def dfs(i,j):
            # base case
            # i oob, j inb
            nonlocal word1
            if i == len(word1) and j < len(word2):
                # insert word2[j] in word1 and call i,j
                word1 += word2[j]
                insert = 1 + dfs(i+1, j+1)
                word1 = word1[:-1]
                return insert
            # i inb, j oob
            if i < len(word1) and j == len(word2):
                return 1 + dfs(i+1, j)
            # i oob, j oob
            if i == len(word1) and j == len(word2):
                return 0
            # recursive case
            # word1 i == word2 j
            insert = remove = replace = len(word1)+1
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            # neq - insert, rm, repl
            else:
                # insert
                word1 = word1[:i] + word2[j] + word1[i:]
                insert = 1 + dfs(i+1, j+1)
                word1 = word1[:i]+word1[i+1:]
                # remove
                remove = 1 + dfs(i+1, j)
                # repl
                replace = 1 + dfs(i+1, j+1)
            # ret min
            return min(insert, remove, replace)
        # return dfs
        return dfs(0,0)