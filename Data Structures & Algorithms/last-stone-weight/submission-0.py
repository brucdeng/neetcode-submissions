import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = [-x for x in stones]
        heapq.heapify(data)
        while len(data)>1:
            x = heapq.heappop(data)
            y = heapq.heappop(data)
            if x==y:
                continue
            elif x > y:
                heapq.heappush(data, y-x)
            else:
                heapq.heappush(data, x-y)
        if data:
            return data[0]*-1
        return 0