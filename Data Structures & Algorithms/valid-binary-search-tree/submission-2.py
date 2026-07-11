# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, leftParentVal, rightParentVal):
            if not node:
                return True

            print("checking", node.val, leftParentVal, rightParentVal)

            if node.left:
                if node.left.val >= node.val:
                    return False
                if leftParentVal and node.left.val <= leftParentVal:
                    return False
                

            if node.right:
                if node.right.val <= node.val:
                    return False
                if rightParentVal and node.right.val >= rightParentVal:
                    return False

            return helper(node.left, leftParentVal, node.val) and helper(node.right, node.val, rightParentVal)

        return helper(root, None, None)