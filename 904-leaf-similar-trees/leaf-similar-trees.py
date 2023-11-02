# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root,lis):
        if not root:
            return
        if not root.left and not root.right:
            lis.append(root.val)
        self.inorder(root.left,lis)
        self.inorder(root.right,lis)
        return lis
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if self.inorder(root1,[]) == self.inorder(root2,[]):
            return True
        return False