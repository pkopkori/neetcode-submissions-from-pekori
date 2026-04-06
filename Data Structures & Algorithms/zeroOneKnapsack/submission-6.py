class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M+1) for _ in range(N)]
        return self.dfs(0, profit, weight, capacity, cache)
    
    def dfs(self, i, profit, weight, capacity, cache):
        # Base case
        if i == len(profit):
            return 0

        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # Skip item i
        cache[i][capacity] = self.dfs(i + 1, profit, weight, capacity, cache)

        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            cache[i][capacity] = max(cache[i][capacity], profit[i] + self.dfs(i + 1, profit, weight, newCap, cache))

        return cache[i][capacity]

