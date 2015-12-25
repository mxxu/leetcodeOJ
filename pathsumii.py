# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None



class Solution(object):

    def pathSum(self, root, sum):

        """

        :type root: TreeNode

        :type sum: int

        :rtype: List[List[int]]

        """

        if not root:
            return []

        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        buf = []

        lefts = self.pathSum(root.left, sum - root.val)
        if lefts:
            for left in lefts:
                buf.append([root.val] + left)

        rights = self.pathSum(root.right, sum - root.val)
        if rights:
            for right in rights:
                buf.append([root.val] + right)

        return buf

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print sol.pathSum(root, 10)
print sol.pathSum(root, 22)
