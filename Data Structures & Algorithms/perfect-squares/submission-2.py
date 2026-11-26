class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, len(dp)):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i], 1 + dp[i - j**2])
                j+=1
        return dp[-1]
