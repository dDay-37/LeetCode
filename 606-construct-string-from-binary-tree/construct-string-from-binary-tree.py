# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans=""
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def a(root):
            if root:
                self.ans+=str(root.val)
                if root.left or root.right:
                    self.ans+="("
                    a(root.left)
                    self.ans+=")"
                if root.right:
                    self.ans+="("
                    a(root.right)
                    self.ans+=")"
            return
        a(root)
        return self.ans
        