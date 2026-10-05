# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pa = self.getAncestors(root, p)
        qa = self.getAncestors(root, q)
        for i in range(len(pa)):
            x = pa.pop()
            if x in qa:
                return x
        return p

    def getAncestors(self, root, node):
        ans = []
        cur = root
        while cur.val!= node.val:
            ans.append(cur)
            if cur.val > node.val:
                cur = cur.left
            else:
                cur = cur.right
        ans.append(node)
        return ans
