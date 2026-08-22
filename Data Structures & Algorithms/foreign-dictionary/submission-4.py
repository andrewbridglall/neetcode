class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # from word list, build edges - compare word to every other word
        edges = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # compare words i and j
                word1, word2 = words[i], words[j]
                k1, k2 = 0, 0
                while k1 < len(word1) and k2 < len(word2):
                    if word1[k1] != word2[k2]:
                        # add to edges
                        # break
                        edges.append([word1[k1], word2[k2]])
                        break
                    # if prefix same and len word1 > len word2 - invalid
                    if k2 == len(word2)-1 and len(word1) > len(word2):
                        return ""
                    k1+=1
                    k2+=1
                    
        # from edges build adj
        adj = {}
        # init adj list from chars in words
        # loop thru all words, if new char, add to set
        uniqueChars = set()
        for word in words:
            for i in range(len(word)):
                if word[i] not in uniqueChars:
                    uniqueChars.add(word[i])
        for char in uniqueChars:
            adj[char] = []
        for u, v in edges:
            adj[u].append(v)    
        
        # run top sort
        # init ds - topsort, visit
        topsort = []
        visit = set()
        path = set()
        # build dfs
        def dfs(c):
            # base case
            # if in path return False
            if c in path:
                return False
            # if already visited return
            if c in visit:
                return True
            # recursive case
            # add to viist
            visit.add(c)
            path.add(c)
            # run dfs on neighbors
            for n in adj[c]:
                if not dfs(n):
                    return False
            # add char to topsort
            topsort.append(c)
            path.remove(c)
            # return
            return True

        # for eveyr node run dfs
        for char in adj:
            if not dfs(char):
                return ""
        # reverse topsort
        topsort.reverse()

        # return top sort -check if need to reverse
        # build string from topsort
        res = ''
        for char in topsort:
            res+=char
        return res
