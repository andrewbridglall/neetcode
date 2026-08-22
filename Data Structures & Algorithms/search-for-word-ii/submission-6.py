class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def prefix(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # init vars
        R,C = len(board), len(board[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        # make trie
        trie = Trie()
        # add all words to trie
        for w in words:
            trie.insert(w)

        # find words in board
        res = set()
        visit = set()
        # make dfs
        def dfs(r,c, prefix):
            # base case
            # r,c oob, rc visited
            if r not in range(R) or c not in range(C) or (r,c) in visit:
                return
            # recursive case
            # add rc to prefix
            # check if prefix in trie - if so, check if is a word - if so add to res
            # else stop
            if not trie.prefix(prefix+board[r][c]):
                return
            if trie.search(prefix+board[r][c]):
                res.add(prefix+board[r][c])
            # add rc to visit
            visit.add((r,c))
            # run dfs up down left right with prefix+rc
            for dr,dc in dirs:
                dfs(r+dr, c+dc, prefix+board[r][c])
            # remove from visit
            visit.remove((r,c))

        # call dfs at every pos in grid
        for r in range(R):
            for c in range(C):
                dfs(r,c, '')

        # if word found add to res
        # convert res set to list
        # return res
        return list(res)