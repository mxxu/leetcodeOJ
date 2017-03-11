# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print s.minDepth(root)