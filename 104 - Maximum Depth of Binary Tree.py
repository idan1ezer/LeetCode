#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root):
    if (root is None):
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(left,right) + 1
