class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x not in "*+/-":
                stack.append(x)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.oper(a, b, x))
        return int(stack.pop())

    def oper(self, a, b, op):
        if op == "+":
            return int(a) + int(b)
        elif op == "*":
            return int(a) * int(b)
        elif op == "/":
            return int(a) / int(b)
        elif op == "-":
            return int(a) - int(b)
