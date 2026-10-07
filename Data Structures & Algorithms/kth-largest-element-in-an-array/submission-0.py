import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numz = [-x for x in nums]
        heapq.heapify(numz)
        for i in range(k-1):
            heapq.heappop(numz)
        return -1 * heapq.heappop(numz)