class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # init vars
        wordList.append(beginWord)
        n = len(wordList)
        adj = defaultdict(list)
        # create graph - neighbors are one diff apaart
        for i in range(n):
            for j in range(i+1, n):
                # compare wordlist i and j
                word1, word2 = wordList[i], wordList[j]
                diff = 0
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        diff +=1
                    if diff > 1:
                        break
                # if 1 diff apart add edge from i to j and j and i
                # undirected edge
                if diff == 1:
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        # edge case - if no endword no soln
        if endWord not in wordList:
            return 0
        # run bfs on graph - shortest path to endword
        # init q, visit
        q = collections.deque()
        visit = set()
        wordPath = 0

        q.append(beginWord)
        visit.add(beginWord)
        wordPath += 1

        while q:
            for _ in range(len(q)):
                # curr = popleft queue
                currWord = q.popleft()
                # go to neighbors of curr
                for nextWord in adj[currWord]:
                    if nextWord == endWord:
                        return wordPath+1
                    if nextWord in visit:
                        continue
                # add neighbors to queue
                # mark neighbors as visited
                    q.append(nextWord)
                    visit.add(nextWord)
            # update length of path
            wordPath +=1

        # return len shortest path, counting beginword
        # default return if endWord not reached from beginWord
        return 0