from utils.treeNode import TreeNode
from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        
        if root.val == subRoot.val:
            self.originalSubroot = subRoot
            if self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right):
                return True
        elif hasattr(self, "originalSubroot"):
            return self.isSubtree(root.left, self.originalSubroot) or self.isSubtree(root.right, self.originalSubroot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
