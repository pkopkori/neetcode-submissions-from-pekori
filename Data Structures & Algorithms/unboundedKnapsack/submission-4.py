class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        dp = [0] * M

        for c in range(M):
            if weight[0] <= c:
                dp[c] = (c // weight[0]) * profit[0]
        
        for i in range(1, N):
            curRow = [0] * M
            for c in range(1, M):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + curRow[c - weight[i]]
                curRow[c] = max(skip, include)
            dp = curRow
        
        return dp[M-1]
