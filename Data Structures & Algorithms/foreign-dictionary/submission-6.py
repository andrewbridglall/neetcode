class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # compare adjacent words
        n = len(words)
        adj = {}
        # add all letters as nodes
        for i in range(n):
            for c in words[i]:
                adj[c] = []

        for i in range(1, n):
            # compare i, i-1
            word1 = words[i-1]
            word2 = words[i]
            k = 0
            while k < min(len(word1), len(word2)) and word1[k] == word2[k]:
                # if chars same skip
                k+=1
                # if chars neq - add to graph
            if k < min(len(word1), len(word2)):
                # add to graph
                adj[word1[k]].append(word2[k])
            # else oob - add nothing
            elif len(word1) > len(word2):
                return ''

        # build graph - added all letter relationships to graph
        # run postorder dfs then reverse
        topsort = []
        visit = set()
        path = set()
        def dfs(node):
            # base case
            if node in path:
                return False
            if node in visit:
                return True
            # recursive case
            path.add(node)
            visit.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
            topsort.append(node)
            path.remove(node)
            return True

        # if cycle found return empty str
        # ret preorder traversal as str
        for i in adj:
            if not dfs(i):
                return ''
        topsort.reverse()
        s = "".join(topsort)
        return s    

