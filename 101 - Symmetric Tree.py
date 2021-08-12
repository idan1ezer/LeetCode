#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(self, root: TreeNode) -> bool:
    if (root is None):
        return True
    return self.isMiror(root.left, root.right)


def isMiror(self, leftRoot, rightRoot):
    if (leftRoot and rightRoot):
        return ((leftRoot.val == rightRoot.val) and (self.isMiror(leftRoot.left,rightRoot.right)) and (self.isMiror(leftRoot.right,rightRoot.left)))
    return leftRoot == rightRoot
