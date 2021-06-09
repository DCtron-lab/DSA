# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        if s is None and t is None:return True
        if t is None:return True
        if s is None and t is not None:return False 
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSameTree(self, s, t):
        if s == None and t == None: return True
        if s == None or t == None: return False
        if s.val != t.val: return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        