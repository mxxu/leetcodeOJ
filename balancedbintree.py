# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def height_balanced(self, root):
        if not root:
            return 0, True
        if not root.left and not root.right:
            return 1, True

        lh, lb = self.height_balanced(root.left)
        rh, rb = self.height_balanced(root.right)
        balanced = abs(lh - rh) <= 1
        return max(lh, rh) + 1, balanced and lb and rb

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, ret = self.height_balanced(root)
        return ret

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
print s.isBalanced(root)