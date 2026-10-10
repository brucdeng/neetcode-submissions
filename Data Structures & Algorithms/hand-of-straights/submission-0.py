import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # make frequency map for all elements
        # get smallest element, see if we can make a group starting from smallest element
        if len(hand) % groupSize != 0:
            return False
        freq = {}
        for val in hand:
            freq[val] = 1 + freq.get(val, 0)
        
        minH = list(freq.keys())
        heapq.heapify(minH)
        while minH:
            smallest = minH[0]
            for val in range(smallest, smallest+groupSize):
                if val in freq.keys() and freq[val]>0:
                    freq[val]-=1
                else:
                    return False
                if freq[val]==0:
                    heapq.heappop(minH)
        return True
