class TrieNode:
    def __init__(self):
        self.characters = {}
        self.word = False
class PrefixTree:

    def __init__(self):
        # init root
        # define trienode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # curr eq root
        curr = self.root
        # iterate thru word
        # if char not found
        # add new trienode
        # word is true
        # return
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = TrieNode()
            curr = curr.characters[c]
        curr.word = True


    def search(self, word: str) -> bool:
        # curr root
        # iterate through word
        # if char not found - ret false
        # ret word bool
        curr = self.root
        for c in word:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        # curr root
        # iterate thru prefix
        # if char not found ret false
        # ret true
        curr = self.root
        for c in prefix:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return True