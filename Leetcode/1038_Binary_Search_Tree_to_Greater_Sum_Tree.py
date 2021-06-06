# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def gst(root, sum):
    if not root:
        return sum
    sum= gst(root.right,sum)
    root.val += sum
    sum = root.val
    return gst(root.left,sum)

class Solution(object):
    def bstToGst(self, root):
        gst(root,0)
        return root
    