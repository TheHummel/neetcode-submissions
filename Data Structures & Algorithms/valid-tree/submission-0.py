class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True

        graph = defaultdict(set)
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        q = deque()
        visited = set()

        q.append((-1, edges[0][0]))
        visited.add(edges[0][0])

        while q:
            u, v = q.popleft()
            for neigh in graph[v]:
                if neigh == u:
                    continue
                if neigh in visited:
                    return False
                q.append((v, neigh))
                visited.add(neigh)

        return len(graph.keys()) == len(visited)