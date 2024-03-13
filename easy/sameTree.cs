/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null){
            return true;
        }

        //if only 1 of them is null, not equal
        if(p == null || q == null){
            return false;
        }

        if(p.val != q.val){
            return false;
        }

        // traverse both subtrees
        bool l = IsSameTree(p.left, q.left);
        bool r = IsSameTree(p.right, q.right);

        // make sure both l and r are TRUE (meaning their subtrees are equal)
        return l && r;
    }
}