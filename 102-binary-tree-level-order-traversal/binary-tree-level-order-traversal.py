# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=deque([root])
        ans=[]
        while q:
            n=len(q)
            tmp=[]
            for i in range(n):
                v=q.popleft()
                if v:
                    tmp.append(v.val)
                    if v.left:
                        q.append(v.left)
                    if v.right:
                        q.append(v.right)
            if tmp:
                ans.append(tmp)
        return ans