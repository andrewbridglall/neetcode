class WordDictionary:

    def __init__(self):
        self.wordset = set()
        

    def addWord(self, word: str) -> None:
        self.wordset.add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            # check set for word
            return word in self.wordset

        else:
            for item in self.wordset:
                if len(item) != len(word):
                    continue
                i = 0
                c = 0
                found = True
                while i < len(word):
                    if word[c] != '.' and item[i] != word[c]:
                        found = False
                        break
                    i+=1
                    c+=1
                if not found:
                    continue
                else:
                    return True
            return False
            # dot in word, so check every word 
            # and iterate through every char
            # when reach dot, skip it
