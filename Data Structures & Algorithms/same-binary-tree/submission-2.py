# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        def check(node1, node2):
            if (not node1 and node2) or (node1 and not node2) :
                self.flag= False
                return
            if node1.val != node2.val:
                self.flag= False
                return

            if node1.left or node2.left:
                if not (node1.left and node2.left):
                    self.flag = False
                    return
                check(node1.left, node2.left)

            if node1.right or node2.right:
                if not (node1.right and node2.right):
                    self.flag = False
                    return
                check(node1.right, node2.right)

        if not p and not q:
            return True

        check(p, q)


        return self.flag