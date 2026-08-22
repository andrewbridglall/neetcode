# implement word dict as prefix tree (trie)
# declare trie node class
class TrieNode:
    def __init__(self):
        self.chars = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        # declare root
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # add word normally to trie
        curr = self.root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TrieNode()
            curr = curr.chars[c]
        curr.word = True

    def search(self, word: str) -> bool:
        # impleemnt as dfs
        def dfs(node, index):    
            curr = node
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.chars.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if c not in curr.chars:
                        return False
                    curr = curr.chars[c]
            return curr.word
        
        return dfs(self.root, 0)
            

