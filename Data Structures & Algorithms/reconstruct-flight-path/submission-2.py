class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # init vars
        n = len(tickets)
        adj = defaultdict(list)
        available = defaultdict(lambda: defaultdict(int))
        # build adj list  from edges
        for src, dst in tickets:
            adj[src].append(dst)
            available[src][dst] +=1

        for src in adj:
            adj[src].sort()
        
        flight_path = []
        flight_path.append('JFK')
        # run dfs on graph
        def dfs(node):
            # base case
            # if no destinations left from node and len path eq edges + 1 wrd
            if (not available[node] or max(available[node].values()) == 0) and len(flight_path) == n+1:
                # print(flight_path)
                return True
            # if no destinations left but not done, return
            if not available[node] or max(available[node].values()) == 0:
                return False
            # recursive case
            # travel to neighbors
            for neighbor in adj[node]:
                # check if neighbor available
                if available[node][neighbor] < 1:
                    continue
                # add neighbor to flight path
                # add neigbhor to visited node
                flight_path.append(neighbor)
                available[node][neighbor] -=1
                # dfs neighbor
                # if dfs true return immediately
                if dfs(neighbor):
                    return flight_path
                # backtrack and remove from viist
                flight_path.pop()
                available[node][neighbor] +=1
        return dfs('JFK')


        