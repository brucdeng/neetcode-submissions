class Solution:
    def hammingWeight(self, n: int) -> int:
        high = 0
        count = 0
        for i in range(32):
            if 2**i > n:
                high = i
                break
        for k in range(high-1, -1, -1):
            if n >= 2**k:
                n -= 2**k
                count +=1
        return count