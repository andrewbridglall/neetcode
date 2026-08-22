class Graph:
    
    def __init__(self):
        self.adj = {} # vertex: [] list of edges

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = []
        if dst not in self.adj:
            self.adj[dst] = []
        self.adj[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False
        if dst not in self.adj:
            return False
        
        if dst in self.adj[src]:
            self.adj[src].remove(dst)
            return True
        else:
            return False
        

    def hasPath(self, src: int, dst: int) -> bool:
        return self.bfs(src, dst)
    
    def bfs(self, src, dst):
        q = collections.deque()
        visit = set()

        q.append(src)
        visit.add(src)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == dst:
                    return True
                for n in self.adj[curr]:
                    q.append(n)
                    visit.add(n)
        return False

