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
            
        if not root.left and not root.right:
            return 1
            
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            
        return self.minDepth(root.left)+1 if root.left else self.minDepth(root.right)+1
        
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print s.minDepth(root)