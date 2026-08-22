class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # bfs soln
        # init ds
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
            
        q = collections.deque()
        visit = set()

        # run bfs
        q.append([0,-1])
        # while q nonempty
        while q:
        # iterate through all elts in q
            for _ in range(len(q)):
        # curr = queue popleft
                node, parent = q.popleft()
        # if curr in visit - cycle detected - ret false
                if node in visit:
                    return False
                visit.add(node)
                for neighbor in adj[node]:
                    if neighbor == parent:
                        continue
                    q.append([neighbor, node])
        # add curr to visit
        # add neighbors of curr to q

        # skip parent node

        # check if visit set len == n
        return len(visit) == n