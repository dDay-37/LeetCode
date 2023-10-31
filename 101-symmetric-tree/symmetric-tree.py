# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def symm(self,left,right):
        if not left and not right:
            return True
        if (not left and right) or (left and not right):
            return False
        if left.val != right.val:
            return False
        return self.symm(left.left , right.right) and self.symm(left.right,right.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symm(root.left, root.right)

    