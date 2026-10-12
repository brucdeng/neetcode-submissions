class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp array, at every num we can either add to the existing subarray or start a new subarray
        maxProduct = nums[0]
        curMax = nums[0]
        curMin = nums[0]
        for i in range(1, len(nums)):
            temp = nums[i]*curMax
            curMax = max(temp, nums[i]*curMin, nums[i])
            curMin = min(nums[i]*curMin, nums[i], temp)
            maxProduct = max(maxProduct, curMax)
        return maxProduct
