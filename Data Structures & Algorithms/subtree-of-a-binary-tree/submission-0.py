# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # BFS on root tree, if subroot detected, run isSameTree
        visited = set([root])
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current.left not in visited and current.left is not None:
                visited.add(current.left)
                queue.append(current.left)
            if current.right not in visited and current.right is not None:
                visited.add(current.right)
                queue.append(current.right)
            if current.val == subRoot.val:
                if self.isSameTree(current, subRoot):
                    return True
        return False

    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if node1 and node2 and node1.val==node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                return False
        return True