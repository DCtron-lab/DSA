# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left https://leetcode.com/discuss/= left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        cache = set()
        return self.bst_helper(root, k, cache)
        
    def bst_helper(self, root, target, cache):
        if not root:
            return False
        if target-root.val in cache:
            return True
        cache.add(root.val)
        return self.bst_helper(root.left,target,cache) or self.bst_helper(root.right,target, cache)


        
