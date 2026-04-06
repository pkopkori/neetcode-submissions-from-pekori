import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, w in edges:
            adj[s].append([d, w])

        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            w1, s1 = heapq.heappop(minHeap)
            if s1 in shortest:
                continue
            shortest[s1] = w1

            for d2, w2 in adj[s1]:
                if d2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, d2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
            
        return shortest

