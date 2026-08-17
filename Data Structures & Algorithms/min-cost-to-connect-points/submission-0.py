class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        n = len(points)
        points = [tuple(p) for p in points]

        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append((manhattan(points[i], points[j]), i, j))

        edges.sort(key=lambda e: e[0])

        parent = list(range(n))


        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        mst_size = 0
        edges_used = 0

        for cost, i, j in edges:
            if union(i, j):
                mst_size += cost
                edges_used += 1
                if edges_used == n - 1:
                    break

        return mst_size

        


