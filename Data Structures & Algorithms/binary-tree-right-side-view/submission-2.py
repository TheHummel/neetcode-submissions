# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rsv = []

        q = deque([root])

        while q:
            rightSide = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                rsv.append(rightSide.val)

        return rsv
        