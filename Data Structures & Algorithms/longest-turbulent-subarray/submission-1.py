class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [[1, 1] for a in arr]
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp[i][1] = dp[i-1][0] + 1
            elif arr[i] < arr[i-1]:
                dp[i][0] = dp[i-1][1] + 1
        return max([max(dp[i]) for i in range(len(dp))])