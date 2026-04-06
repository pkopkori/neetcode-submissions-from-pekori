class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # adjececy list
        adj = {}
        for i in range(n):
            adj[i] = []
        for n1, n2, w in edges:
            adj[n1].append([n2, w])
            adj[n2].append([n1, w])
        
        minHeap = [[0, 0]]
        res = 0
        visit = set()
        while minHeap and len(visit) < n:
            weight, v = heapq.heappop(minHeap)
            if v in visit:
                continue

            res += weight
            visit.add(v)
            for neighbor, weight in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])

        return res if len(visit) == n else -1 

