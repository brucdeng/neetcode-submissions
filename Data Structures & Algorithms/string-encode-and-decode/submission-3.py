class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + '#' + s
        return ans
    def decode(self, s: str) -> List[str]:
        #return [s]
        res = []
        tempLen = 0
        i = 0
        while i < len(s):
            if s[i]=='#':
                res.append(s[i+1:i+1+tempLen])
                i = i+1+tempLen
                tempLen = 0
            else:
                tempLen = tempLen*10+int(s[i])
                i+=1
        return res