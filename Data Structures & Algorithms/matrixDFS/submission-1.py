class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, grid, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 1 or (r, c) in visited:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visited.add((r, c))
            count = 0
            count += dfs(r-1, c, grid, visited)
            count += dfs(r+1, c, grid, visited)
            count += dfs(r, c-1, grid, visited)
            count += dfs(r, c+1, grid, visited)
            
            visited.remove((r, c))
            return count
        
        return dfs(0, 0, grid, set())
