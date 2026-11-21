class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        cap = high
        def canFinish(days, weights, cap):
            dayCount = 1
            total = 0
            for x in weights:
                if x + total <= cap:
                    total+=x
                else:
                    total = x
                    dayCount+=1
            if dayCount > days:
                return False
            return True
        while (low <= high):
            mid = (high+low)//2
            if canFinish(days, weights, mid):
                high = mid -1
                cap = min(cap, mid)
            else:
                low = mid + 1
        return cap