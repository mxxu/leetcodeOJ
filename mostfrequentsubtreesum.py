# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.m = {}
        self.subsum(root)
        # s = sorted(self.m.items(), key=lambda e: e[1], reverse=True)
        maxs = max(self.m.values())
        return [k for k, v in self.m.iteritems() if v == maxs]
        
    def subsum(self, root):
        if not root:
            s = 0
        else:
            s = root.val + self.subsum(root.left) + self.subsum(root.right)
            self.m[s] = self.m.get(s, 0) + 1
        return s
        
s = Solution()
t = TreeNode(5)
t.left = TreeNode(2)
t.right = TreeNode(-3)
print s.findFrequentTreeSum(t)

t.right = TreeNode(-5)
print s.findFrequentTreeSum(t)