# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        io_map = {node: i for i, node in enumerate(inorder)}
        po_idx = 0

        def traverse(l, r):
            nonlocal po_idx

            if l > r:
                return None

            node_val = preorder[po_idx]
            po_idx += 1
            node = TreeNode(val=node_val)

            m = io_map[node_val]

            node.left = traverse(l, m-1)
            node.right = traverse(m+1, r)

            return node

        return traverse(0, len(inorder)-1)

