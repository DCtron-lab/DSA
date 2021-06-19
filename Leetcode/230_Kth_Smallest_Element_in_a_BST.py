# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)
        return arr
class Solution(object):
    def kthSmallest(self, root, k):
        arr = []
        new_root = inorder(root, arr)
        return new_root[k-1]
        