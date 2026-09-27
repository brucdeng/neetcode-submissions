import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #time to eat x bananas: ceil(x/k)
        #k <= max(piles)
        low = 1
        high = max(piles)
        ans = high
        while low<=high:
            mid = low+(high-low)//2
            total = sum([math.ceil(x/mid) for x in piles])
            if total > h:
                low = mid+1
            elif total <=h:
                ans = mid
                high = mid-1
        return ans
