class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}
        for s, d, w in edges:
            adj[s].append([d, w])
        
        shortestPaths = {i: -1 for i in range(n)}
        visit = set()
        minHeap = [] # [cumulative weight, dst]

        minHeap.append([0,src])
        
        while minHeap:
            weight, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue
            
            visit.add(dst)
            shortestPaths[dst] = weight
            
            for n1, w1 in adj[dst]:
                if n1 not in visit:
                    heapq.heappush(minHeap, [weight+w1, n1])
        
        return shortestPaths

