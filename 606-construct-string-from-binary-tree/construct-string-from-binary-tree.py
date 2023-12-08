# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        ans=[]
        def DLR( root):
            if not root:
                return
            ans.append('(')     
            ans.append(str(root.val)) 
            if not root.left and root.right:
                ans.append('()')
            DLR(root.left)
            DLR(root.right)
            ans.append(')') 
        DLR(root)
        return "".join(ans)[1:-1]
        