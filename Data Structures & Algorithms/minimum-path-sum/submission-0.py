class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for c in r] for r in grid]
        dp[0][0] = grid[0][0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if c+1 < len(grid[0]):
                    dp[r][c+1] = min(dp[r][c+1], dp[r][c] + grid[r][c+1])
                if r+1 < len(grid):
                    dp[r+1][c] = min(dp[r+1][c], dp[r][c] + grid[r+1][c])
        return dp[-1][-1]