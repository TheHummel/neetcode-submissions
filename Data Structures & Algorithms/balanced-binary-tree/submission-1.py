# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        self.balanced = True

        
        def dfs(node, depth):
            leftHeight = depth
            rightHeight = depth

            if node.left:
                leftHeight = dfs(node.left, depth+1)

            if node.right:
                rightHeight = dfs(node.right, depth+1)

            print(node.val, leftHeight, rightHeight)

            if abs(leftHeight-rightHeight) > 1:
                self.balanced = False

            return max(leftHeight, rightHeight)

        dfs(root, 0)


        return self.balanced 

        

        