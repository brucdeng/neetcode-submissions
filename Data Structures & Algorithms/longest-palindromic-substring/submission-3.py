class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp = [[False for i in range(len(s))] for j in range(len(s))]
        # a, b, aba, a, bab, ababd, b, abd, 
        ans = s[0]
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r <= len(s)-1:
                if s[l]!=s[r]:
                    break
                if len(s[l:r+1]) > len(ans):
                    ans = s[l:r+1]
                l-=1
                r+=1
            l = i
            r = i+1
            while l >= 0 and r <= len(s)-1:
                if s[l]!=s[r]:
                    break
                if len(s[l:r+1]) > len(ans):
                    ans = s[l:r+1]
                l-=1
                r+=1
        return ans