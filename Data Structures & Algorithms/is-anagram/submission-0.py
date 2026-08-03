class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = list(s)
        newS.sort()
        newT = list(t)
        newT.sort()
        return newS==newT