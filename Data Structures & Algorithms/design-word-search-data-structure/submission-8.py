class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        # init as trie
        # init root
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        # make dfs
        # run dfs
        
        # build recursive search
        def dfs(root, startIndex):
            # base case
            # recurisve case
            curr = root
            for i in range(startIndex, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.word

        return dfs(self.root, 0) #place at end