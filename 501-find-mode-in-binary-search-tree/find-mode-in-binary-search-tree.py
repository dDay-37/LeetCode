# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.lis = []
        def abc(root):
            if not root:
                return
            else:
                print("root.val",root.val)
                self.lis.append(root.val)
                abc(root.left)
                abc(root.right)
        abc(root)
        f = collections.Counter(self.lis)
        m = max(f.values())
        return [x for x in f if f[x] == m]