# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    def dfs(self,node):
        if not node:
            return [0,0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        Sum = left[0] + right[0] + node.val
        Count = left[1] + right[1] + 1

        if Sum // Count == node.val:
            self.result += 1
        return [Sum,Count]

    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dfs(root)
        return self.result