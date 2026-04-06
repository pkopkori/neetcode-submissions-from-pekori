class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        dp = [[0] * M for _ in range(N)]

        # fill out first row
        for c in range(M):
            if weight[0] <= c:
                dp[0][c] = (c // weight[0]) * profit[0]
        
        for i in range(1, N):
            for c in range(1, M):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i][c - weight[i]]
                dp[i][c] = max(skip, include)
        
        return dp[N-1][M-1]

