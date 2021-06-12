# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dia(node):
    if not node:
        return 0, 0
    lp,lw = dia(node.left)
    rp,rw = dia(node.right)
    
    return 1+ max(lp,rp), max(lw , rw , 1+ lp + rp)

class Solution(object):
    def diameterOfBinaryTree(self, root):
        return dia(root)[1] - 1   
        