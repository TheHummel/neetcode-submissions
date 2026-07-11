# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max = 0

        def dfs(node, depth):
            leftHeight = depth
            rightHeight = depth

            if node.left:
                leftHeight = dfs(node.left, depth + 1)

            if node.right:
                rightHeight = dfs(node.right, depth + 1) 

            print(node.val, leftHeight, rightHeight, depth)

            self.max = max(self.max, leftHeight + rightHeight - 2*depth)

            return max(leftHeight, rightHeight)

        dfs(root, 0)

        return self.max
        