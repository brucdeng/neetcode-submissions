class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        cur_sum = nums[0]
        cur_min_sum = nums[0]
        for x in nums[1:]:
            cur_sum = max(x, cur_sum+x)
            cur_min_sum = min(x, cur_min_sum+x)
            max_sum = max(max_sum, cur_sum)
            min_sum = min(cur_min_sum, min_sum)
        if min_sum == sum(nums):
            return max_sum
        return max(max_sum, sum(nums) - min_sum)