class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        m = int((h-l)/2)
        while (l <= h):
            if nums[m]==target:
                return m
            elif nums[m] > target:
                h=m-1
                m-=int((m-l+1)/2)
            else:
                l=m+1
                m+=int((h-m+1)/2)
        return -1