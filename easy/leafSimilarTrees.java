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

class Solution {
    public List<Integer> getSequence(TreeNode root, List<Integer> nodes){
        if(root.left == null && root.right == null){
            nodes.add(root.val);

            return nodes;
        }

        if(root.left != null){
            getSequence(root.left, nodes);
        }

        if(root.right != null){
            getSequence(root.right, nodes);
        }

        return nodes;
    }

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();

        return getSequence(root1, a).equals(getSequence(root2, b));
    }
}