# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            self.moves += abs(left_excess) + abs(right_excess)
            return node.val + left_excess + right_excess - 1

        dfs(root)
        return self.moves

# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (due to recursion stack).