class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null)
            return null;
        
        if (key > root.val)
            root.right = deleteNode(root.right, key);
        else if (key < root.val)
            root.left = deleteNode(root.left, key);
        else {
            if (root.left == null || root.right == null) {
                if (root.left != null)
                    root = root.left;
                else 
                    root = root.right;
                // return root;
            } else {
                TreeNode min = root.right;
                while(min.left != null) min = min.left;
                root.val = min.val;
                root.right = deleteNode(root.right, min.val);   
            }
        }
        return root;
    }
}