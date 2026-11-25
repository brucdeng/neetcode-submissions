class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp = [0 for num in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        ans = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = nums[i] + dp[i-2]
            ans = max(temp, ans)
            dp[i] = max(temp, dp[i-1])

        dp2 = [0 for num in nums]
        dp2[1] = nums[1]
        for i in range(2, len(nums)):
            temp = nums[i] + dp2[i-2]
            ans = max(temp, ans)
            dp2[i] = max(temp, dp2[i-1])
        return max(dp[-2], dp2[-1])