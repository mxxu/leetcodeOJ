# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        m = {}
        queue = [(root, 0)]
        maxrow = 0
        while queue:
            node, row = queue.pop(0)
            if not node:
                continue
            maxrow = max(maxrow, row)
            if row in m:
                if m[row] < node.val:
                    m[row] = node.val
            else:
                m[row] = node.val
            queue.append((node.left, row+1))
            queue.append((node.right, row+1))
        return [m[i] for i in range(maxrow+1)]
s = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print s.largestValues(root)