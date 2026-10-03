# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if (node1 is None and node2 is None):
                return True
            if node1 and node2 and node1.val==node2.val:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            else:
                return False
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
        #return dfs(p, q)
    