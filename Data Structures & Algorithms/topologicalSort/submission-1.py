class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
        
        topoSort = []
        visit = set()
        path = set()
        for i in range(n):
            if not self.dfs(i, adj, visit, path, topoSort):
                return []
        topoSort.reverse()
        return topoSort

    def dfs(self, src, adj, visit, path, topoSort):
        if src in path:
            return False
        if src in visit:
            return True
        
        path.add(src)
        for neighbor in adj[src]:
            if not self.dfs(neighbor, adj, visit, path, topoSort):
                return False
        path.remove(src)
        visit.add(src)
        topoSort.append(src)

        return True

        