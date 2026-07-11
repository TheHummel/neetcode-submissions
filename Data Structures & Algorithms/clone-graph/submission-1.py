"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #n0 = Node(node.val, node.neighbours
        if not node:
            return node

        queue = deque()
        #visited = set()

        queue.append(node)

        n0 = Node(node.val)

        old_new_map = {node: n0}

        while queue:
            n = queue.pop()

            #visited.add(n)
            n_new = old_new_map[n]

            for neigh in n.neighbors:

                if neigh in old_new_map:
                    neigh_new = old_new_map[neigh]

                else:
                    neigh_new = Node(neigh.val)
                    old_new_map[neigh] = neigh_new

                    queue.append(neigh)

                n_new.neighbors.append(neigh_new)

        return n0
        #return node
        