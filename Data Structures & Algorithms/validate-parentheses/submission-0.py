from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '{': '}', '[': ']'}
        stack = deque()
        for x in s:
            if x in dic:
                stack.append(x)
            else:
                if len(stack)==0:
                    return False
                else:
                    if dic[stack[-1]]==x:
                        stack.pop()
                    else:
                        return False
        return len(stack)==0