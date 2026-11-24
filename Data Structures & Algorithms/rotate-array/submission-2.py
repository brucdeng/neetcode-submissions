class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = (len(nums) - k) % len(nums)
        temp = []
        for i in range(len(nums)):
            temp.append(nums[(start+i) % len(nums)])
        for i in range(len(nums)):
            nums[i] = temp[i]
        
        