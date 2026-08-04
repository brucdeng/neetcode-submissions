import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for x in nums:
            if x in map:
                map[x]+=1
            else:
                map[x] = 1
        ls = [(-val, key) for key, val in map.items()]
        heapq.heapify(ls)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(ls)[1])
        return ans