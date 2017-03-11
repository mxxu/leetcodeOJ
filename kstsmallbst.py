# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        n = 0
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            n += 1
            if n == k:
                return node.val
                
            node = node.right
        return node.val
        
if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.right = TreeNode(10)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(6)
    root.right.left = TreeNode(9)
    
    for i in range(1, 8):
        print Solution().kthSmallest(root, i)