# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a1=[]
        a2=[]
        def fun(root,a):
            if root.left:
                fun(root.left,a)
            if root.right:
                fun(root.right,a)
            if not root.left and not root.right:
                a.append(root.val)
            return a
        fun(root1,a1)
        fun(root2,a2)
        return a1==a2