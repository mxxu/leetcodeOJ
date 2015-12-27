# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        buf = []
        path = ''
        stack = []
        stack.append((path, root))

        while stack:
            print stack
            path, node = stack.pop()
            print path, node
            path = '%s->%s' % (path, node.val) if path else str(node.val)
            if not node.left and not node.right:
                buf.append(path)
                continue
            if node.left:
                stack.append((path, node.left))
            if node.right:
                stack.append((path, node.right))
        return buf

t = TreeNode(1)
t.left = TreeNode(2)
s = Solution()
print s.binaryTreePaths(t)
