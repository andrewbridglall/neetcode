class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def searchPrefix(self, prefix: str):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add list of words to trie
        trie = Trie()
        for word in words:
            trie.add(word)
        # iterate through grid and run dfs on all prefixes along path
        R,C = len(board), len(board[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        res = []

        def dfs(r,c,prefix, visit, res):
            # base case
            # if r,c oob or visited - return
            if r not in range(R) or c not in range(C) or (r,c) in visit:
                return
            # add char at r,c to prefix
            prefix += board[r][c]
            visit.add((r,c))
            # check if prefix in trie
            if trie.searchPrefix(prefix):
            # if so, check if prefix is a word in trie and add to res if so
                if trie.search(prefix) and prefix not in res:
                    res.append(prefix)
            # recursive case
            # run dfs on all 4 directions
                for dr,dc in dirs:
                    dfs(r+dr, c+dc, prefix, visit, res)
            # pop char at r,c from prefix, remove from visit
            prefix = prefix[:-1]
            visit.remove((r,c))
            return
            # return


        for r in range(R):
            for c in range(C):
                dfs(r,c, "", set(), res)
        # if word found add to res list and return at end
        return res