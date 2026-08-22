class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # bf
        # run dfs
        def dfs(i,j):
            # base case
            # i oob
            if i == len(word1):
                # insert remaining chars in word2
                return len(word2) - j
            # i inb j oob
            if j == len(word2):
                # delete remaining chars in word1
                return len(word1) - i
            # recursive case
            # chars i j eq
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            # chars i j neq - insert, remove, repl
            else:
                insert = 1 + dfs(i, j+1)
                remove = 1 + dfs(i+1, j)
                replac = 1 + dfs(i+1, j+1)
                return min(insert, remove, replac)
            
            # return min ins, rm, repl
        # return dfs
        return dfs(0,0)