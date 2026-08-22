class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # build adj list
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(len(edges)):
            src, dst, prob = edges[i][0], edges[i][1], succProb[i]
            adj[src].append([dst, prob])
            adj[dst].append([src, prob])
        # declare maxheap, max prob map
        maxheap = []
        probmap = defaultdict(float)
        # add start to maxheap
        maxheap.append([-1*(1), start_node, start_node])
        # while maxheap:
            # pop from max => prob, src, dst
            # if dst in map already skip
            # add to map with prob
            # add neighbors to max with product of probs
        while maxheap:
            negprob, src, dst = heapq.heappop(maxheap)
            if dst in probmap:
                continue
            
            prob = -1*negprob
            probmap[dst] = prob

            for n, p in adj[dst]:
                if n in probmap:
                    continue
                heapq.heappush(maxheap, [-1*(prob*p), dst, n])

        # return map[end]
        return probmap[end_node]

