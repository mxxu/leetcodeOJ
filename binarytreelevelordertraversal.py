# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        # m = {}
        queue = [(root, 0)]
        # maxrow = 0
        lastrow = -1
        curr_buf = []
        buf = []
        while queue:
            node, row = queue.pop(0)
            if not node:
                continue
            if lastrow != row:
                if curr_buf:
                    buf.insert(0, curr_buf)
                lastrow = row
                curr_buf = []
            curr_buf.append(node.val)
            # maxrow = max(maxrow, row)
            # if row in m:
                # m[row].append(node.val)
            # else:
                # m[row] = [node.val]
            queue.append((node.left, row+1))
            queue.append((node.right, row+1))
            
        if curr_buf:
            buf.insert(0, curr_buf)
        return buf
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# root.right.right = TreeNode(9)
print s.levelOrder(root)