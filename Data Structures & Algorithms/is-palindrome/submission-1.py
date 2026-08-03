class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
        newS = []
        for x in s:
            if x in alpha:
                newS.append(x)
        i=0
        j=len(newS)-1
        while (i < j):
            if (newS[i]!=newS[j]):
                return False
            else:
                i+=1
                j-=1
        return True