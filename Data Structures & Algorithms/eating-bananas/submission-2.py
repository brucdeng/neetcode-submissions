import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        low = 1
        high = k
        while low <= high:
            mid = (low+high)//2
            hours = sum([math.ceil(p/mid) for p in piles])
            if hours > h:
                low = mid+1
            elif hours <=h:
                high = mid -1
                k = min(mid, k)
        return k
