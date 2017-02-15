# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxdepth = 0
        queue = [(root, 0)]
        depth_leaf = {}
        
        while queue:
            node, depth = queue.pop(0)
            maxdepth = depth
            if node.left or node.right:
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
                continue
            if depth not in depth_leaf:
                depth_leaf[depth] = node.val
        return depth_leaf[maxdepth]
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
print s.findBottomLeftValue(root)