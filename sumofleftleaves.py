# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        return self.go(root.left, True) + self.go(root.right, False)
        
    def go(self, root, isleft):
        if not root:
            return 0
        if not root.left and not root.right:
            if isleft:
                return root.val
            return 0
        return self.go(root.left, True) + self.go(root.right, False)
        
sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print sol.sumOfLeftLeaves(root)