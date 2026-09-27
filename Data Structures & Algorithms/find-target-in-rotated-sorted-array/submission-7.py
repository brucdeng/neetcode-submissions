class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findMinIndex(nums)
        l, r = 0, len(nums)-1
        if minIndex > 0 and nums[l] <= target <= nums[minIndex-1]:
            r = minIndex-1
        else:
            l = minIndex
        while l <=r:
            m = (r+l)//2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                return m
        return -1

    def findMinIndex(self, nums):
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (high+low)//2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        return low