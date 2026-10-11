class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        ans = max(dp[0], dp[1])
        for i in range(2, len(nums), 1):
            temp = nums[i] + dp[i-2]
            if temp > ans:
                ans = temp
            dp[i] = max(temp, dp[i-1])
        return ans