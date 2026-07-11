# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good_nodes = 0

        def dfs(node, maxim):
            maxim = max(maxim, node.val)
            if node.val >= maxim:
                self.good_nodes += 1
            if node.left:
                dfs(node.left, maxim)
            if node.right:
                dfs(node.right, maxim)

        dfs(root, -101)

        return self.good_nodes