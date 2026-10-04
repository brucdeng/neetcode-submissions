import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            heapq.heappush(pq, (math.sqrt((point[0]**2 + point[1]**2)), point))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans