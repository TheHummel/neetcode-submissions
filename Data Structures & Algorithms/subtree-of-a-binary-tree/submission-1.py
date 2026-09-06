# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if bool(root1) != bool(root2):
                return False
            if not root1 and not root2:
                return True
            if root1.val != root2.val:
                return False
            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

        def dfs(node):
            if not node:
                return False
            if sameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)