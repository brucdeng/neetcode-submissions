# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, maxSoFar):
            nonlocal ans
            if node is None:
                return 0
            if node.val>=maxSoFar:
                ans+=1
                maxSoFar = node.val
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)
        dfs(root, root.val)
        return ans
        