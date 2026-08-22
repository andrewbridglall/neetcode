class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # run dijkstra's - shortest path
        # init vars
        adj = defaultdict(list)
        # build adj list
        for s,d,w in flights:
            adj[s].append([d,w])
        # from src as starting point find shortest path to all ndese in graph
        minheap = []
        
        for d,w in adj[src]:
            heapq.heappush(minheap, [w, d, 1]) # price, node, counter
        
        # add edges from serc to minheap
        # while minheap non empty 
        while minheap:
        # pop shortest path from minheap
            price, node, count = heapq.heappop(minheap)
            # add check
            # if node eq dst and count leq k+1 wrd
            if node == dst and count <= k+1:
                return price
            # if count == k+1 (and not dst) continue -reached node 
            # that is not dst and already used max stops allowed
            if node != dst and count == k+1:
                continue
        # go to neighbors
            for neighbor,p in adj[node]:
                heapq.heappush(minheap, [price+p, neighbor, count+1])
        # default return -1
        return -1