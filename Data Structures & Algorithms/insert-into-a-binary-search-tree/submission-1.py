# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        def dfs(root):
            if not root:
                return
            if root.left and root.right:
                if val > root.val:
                    dfs(root.right)
                else:
                    dfs(root.left)
            elif root.left and not root.right:
                if val > root.val:
                    root.right = node
                    return
                else:
                    dfs(root.left)
            elif not root.left and root.right:
                if val < root.val:
                    root.left = node
                    return
                else:
                    dfs(root.right)
            else:
                if val > root.val:
                    root.right = node
                    return
                else:
                    root.left = node
                    return
        dfs(root)
        return root
        