import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        longest = 1
        temp = 1
        prev = heapq.heappop(nums)
        while nums:
            cur = heapq.heappop(nums)
            if cur==prev+1:
                temp+=1
                if temp > longest:
                    longest = temp
            elif cur!=prev:
                if temp > longest:
                    longest = temp
                temp = 1
            prev= cur
        return longest