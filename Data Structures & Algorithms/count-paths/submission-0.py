class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0 for i in range(n)] for k in range(m)]
        for i in range(n):
            ans[0][i] = 1
        for i in range(m):
            ans[i][0] = 1
        for r in range(1, m):
            for c in range(1, n):
                ans[r][c] = ans[r-1][c]+ans[r][c-1]
        return ans[m-1][n-1]
