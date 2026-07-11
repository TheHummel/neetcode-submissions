# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-infinity")


        #def calc_max_path(node):

        
        def process_node(node):
            if not node:
                return 0

            leftVal = max(0, process_node(node.left))
            rightVal = max(0, process_node(node.right))

            self.maxSum = max(node.val + leftVal + rightVal, self.maxSum)

            return node.val + max(leftVal, rightVal)

        process_node(root)

        return self.maxSum
