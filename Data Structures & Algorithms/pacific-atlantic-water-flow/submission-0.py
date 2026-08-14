class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        def neighbours(node):
            i, j = node
            neighs = set()
            if i>0:
                neighs.add((i-1, j))
            if i<n-1:
                neighs.add((i+1, j))
            if j>0:
                neighs.add((i, j-1))
            if j<m-1:
                neighs.add((i, j+1))
            return neighs

        visited_pacific = set()
        q_pacific = deque()

        for j in range(m):
            q_pacific.append((0, j))
            visited_pacific.add((0, j))

        for i in range(n):
            q_pacific.append((i, 0))
            visited_pacific.add((i, 0))

        while q_pacific:
            node = q_pacific.popleft()
            level = heights[node[0]][node[1]]
            neighs = neighbours(node)
            for neigh in neighs:
                if heights[neigh[0]][neigh[1]] >= level and neigh not in visited_pacific:
                    visited_pacific.add(neigh)
                    q_pacific.append(neigh)

        visited_atlantic = set()
        q_atlantic = deque()

        for j in range(m):
            q_atlantic.append((n-1, j))
            visited_atlantic.add((n-1, j))

        for i in range(n):
            q_atlantic.append((i, m-1))
            visited_atlantic.add((i, m-1))

        while q_atlantic:
            node = q_atlantic.popleft()
            level = heights[node[0]][node[1]]
            neighs = neighbours(node)
            for neigh in neighs:
                if heights[neigh[0]][neigh[1]] >= level and neigh not in visited_atlantic:
                    visited_atlantic.add(neigh)
                    q_atlantic.append(neigh)

        return [list(node) for node in visited_pacific & visited_atlantic]
