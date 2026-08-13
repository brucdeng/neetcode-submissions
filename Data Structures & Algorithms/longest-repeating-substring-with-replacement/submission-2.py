class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0 
        r=0
        max_freq = 0
        ans = 0
        while l < len(s) and r < len(s):
            #if r - l - max_freq <=k:
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]] = 1
            max_freq = max(max_freq, freq[s[r]])
            while r-l+1 - max_freq > k:
                freq[s[l]]-=1
                l+=1
        
            ans = max(ans, r-l+1)
            r+=1
        return ans
            
            
            
            