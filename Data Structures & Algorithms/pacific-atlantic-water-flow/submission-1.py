class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(starts):
            visited = [[False] * m for _ in range(n)]
            q = deque(starts)
            for r, c in starts:
                visited[r][c] = True

            while q:
                r, c = q.popleft()
                level = heights[r][c]
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and heights[nr][nc] >= level:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        
            return visited

        pacific_starts = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]
        atlantic_starts = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r in range(n) for c in range(m) if pacific[r][c] and atlantic[r][c]]