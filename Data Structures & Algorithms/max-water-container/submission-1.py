class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = 0
        r = len(heights)-1
        while (l < r):
            ans = max(ans, (r-l)*min(heights[r], heights[l]))
            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        return ans