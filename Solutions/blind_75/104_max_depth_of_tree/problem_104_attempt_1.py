from typing import Optional
from utils.treeNode import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(node, curDepth):
            if node == None:
                return curDepth
            curDepth += 1
            return max(getDepth(node.left, curDepth), getDepth(node.right, curDepth))
        return getDepth(root, 0)