class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #map = {}
        ans = 0
        cur =0
        l = 0
        r = 0
        while l < len(s) and r < len(s):
            if s[r] not in s[l:r]:
                cur+=1
                r+=1
            else:
                l+=1
                cur-=1
            ans = max(ans, cur)
        return ans