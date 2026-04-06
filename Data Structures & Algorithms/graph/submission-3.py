class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True
        
    def hasPath(self, src: int, dst: int) -> bool:
        # visited = set()
        # return self._dfs(src, dst, visited)
        return self._bfs(src, dst)
    
    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True
        return False
    
    def _bfs(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque([src])
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            visited.add(curr)
            for neighbor in self.adj_list[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
            





