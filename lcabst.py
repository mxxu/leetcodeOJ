# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
            
        minv, maxv = min(p.val, q.val), max(p.val, q.val)
        
        if minv <= root.val <= maxv:
            return root    
        elif root.val < minv:
            return self.lowestCommonAncestor(root.right, p, q)  
        else:
            return self.lowestCommonAncestor(root.left, p, q)
            
if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    s = Solution()
    ret = s.lowestCommonAncestor(root, root.left, root.left.right)
    print ret.val