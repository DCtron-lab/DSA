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
class Solution{
    // tc - N sc -  N set of size can go till N
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> set = new HashSet<>();
        return helper(root, set,k);        
    }
    
    private boolean helper(TreeNode root, Set<Integer> set, int k){
        if(root==null) return false;
        if(set.contains(k-root.val)) return true; 
        set.add(root.val);
        return helper(root.left, set, k) 
            || helper(root.right, set, k);
    }
}