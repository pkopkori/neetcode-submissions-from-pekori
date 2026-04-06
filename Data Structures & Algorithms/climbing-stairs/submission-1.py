class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        return self.dfs(n, cache)
    
    def dfs(self, i, cache):
        if i < 0:
            return 0
        if i == 0:
            return 1
        
        if cache[i] != -1:
            return cache[i]
        
        cache[i] = self.dfs(i-1, cache) + self.dfs(i-2, cache)
        return cache[i]

        