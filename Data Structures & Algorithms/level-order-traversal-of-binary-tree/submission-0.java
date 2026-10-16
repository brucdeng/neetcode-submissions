/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
//import java.util.*;
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q = new ArrayDeque<>();
        List<List<Integer>> res = new ArrayList<>();
        if (root==null) {
            return res;
        }
        q.offer(root);
        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int i = q.size(); i>0; i--) {
                TreeNode t = q.poll();
                if (t!=null) {    
                    level.add(t.val);
                    if (t.left != null) {
                        q.add(t.left);
                    }
                    if (t.right != null) {
                        q.add(t.right);
                    }
                    
                }
            }
            if (level.size() > 0) {
                res.add(level);
            }
            
        }
        return res;
    }
}
