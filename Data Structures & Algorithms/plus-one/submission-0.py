class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        stack = []
        for x in digits:
            stack.append(x)
        carry = 1
        while stack:
            digit = stack.pop() + carry
            ans.append(digit%10)
            carry = digit//10
        if carry:
            ans.append(carry)
        ans.reverse()
        return ans