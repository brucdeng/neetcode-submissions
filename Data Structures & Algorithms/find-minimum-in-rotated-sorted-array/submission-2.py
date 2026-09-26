class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        ans = nums[low]
        while low <=high:
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            mid = (high+low)//2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid+1
            else:
                high = mid -1 
        return ans