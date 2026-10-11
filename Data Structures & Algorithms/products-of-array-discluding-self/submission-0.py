class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 6
        # 1 1 2 8
        # 48 24 6 1
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for i in range(1, len(nums)):
            if i ==1:
                prefix[i] = nums[i-1]
            else:
                prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            if i == len(nums)-2:
                suffix[i] = nums[i+1]
            else:
                suffix[i] = nums[i+1]*suffix[i+1]
        return [x*y for x, y in zip(prefix, suffix)]