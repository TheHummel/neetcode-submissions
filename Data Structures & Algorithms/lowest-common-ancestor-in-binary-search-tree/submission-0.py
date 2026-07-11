# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(r, a, b):
            if a.val == r.val or b.val == r.val:
                return r
            if a.val < r.val and b.val < r.val:
                return traverse(r.left, a, b)
            if a.val > r.val and b.val > r.val:
                return traverse(r.right, a, b)
            return r

        return traverse(root, p, q)