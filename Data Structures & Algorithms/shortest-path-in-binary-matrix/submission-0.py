class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        queue = deque()
        visit = set((0, 0))
        queue.append((0, 0))
        length = 1
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == N - 1 and c == N - 1:
                    return length

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        continue
                    if grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1

        return -1