# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        if (not p1 or not p2):
            return False
        while True:
            if (p1.next):
                p1 = p1.next
            else:
                return False
            if (p2.next):
                p2 = p2.next
                if (p2.next):
                    p2=p2.next
                else:
                    return False
            else:
                return False
            if p1==p2:
                return True