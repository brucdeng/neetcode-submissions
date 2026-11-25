class Solution:
    def validPalindrome(self, s: str) -> bool:
        #ccbcd
        l = 0
        r = len(s)-1
        while l < r:
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            else:
                return self.palindrome(s[l+1:r+1]) or self.palindrome(s[l:r])
        return True

    def palindrome(self, s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
