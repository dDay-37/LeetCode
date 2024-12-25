class Solution(object):
    def largestValues(self, root):
        result = []
        
        if not root:
            return result
        q = deque()
        
        q.append(root)

        
        while q:
            level_len = len(q)
            maximum = float('-inf')
            for _ in range(level_len):
                node = q.popleft()
                maximum = max(maximum, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(maximum)
        return result