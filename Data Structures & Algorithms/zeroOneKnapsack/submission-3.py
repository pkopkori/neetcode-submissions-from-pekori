class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        cache = [[-1] * M for _ in range(N)]
        return self.dfs(0, profit, weight, capacity, cache) 

    def dfs(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0

        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # skip item i
        cache[i][capacity] = self.dfs(i + 1, profit, weight, capacity, cache)

        # include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfs(i + 1, profit, weight, newCap, cache)
            cache[i][capacity] = max(cache[i][capacity], p)
        
        return cache[i][capacity]
