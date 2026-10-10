class Solution:
    def checkValidString(self, s: str) -> bool:
        leftS = []
        starS = []
        for i, char in enumerate(s):
            if char == "(":
                leftS.append(i)
            elif char == "*":
                starS.append(i)
            else:
                if leftS:
                    leftS.pop()
                elif starS:
                    starS.pop()
                else:
                    return False
        while starS and leftS:
            if leftS.pop()> starS.pop():
                return False
        return len(leftS)==0