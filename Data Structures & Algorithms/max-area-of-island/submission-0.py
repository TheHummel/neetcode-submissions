class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0

        n = len(grid)
        m = len(grid[0])

        marked = [[0 for j in range(m)] for i in range(n)]

        def neighbours(i, j):
            neighs = []
            if i>0 and grid[i-1][j]:
                neighs.append((i-1, j))
            if i<n-1 and grid[i+1][j]:
                neighs.append((i+1, j))
            if j>0 and grid[i][j-1]:
                neighs.append((i, j-1))
            if j<m-1 and grid[i][j+1]:
                neighs.append((i, j+1))

            return neighs

        def bfs(i, j, count):
            queue = deque()
            queue.append((i, j))
            visited = set()
            visited.add((i, j))

            size = 0
            
            while queue:
                i, j = queue.pop()
                marked[i][j] = count
                size += 1
                neighs = neighbours(i, j)
                for neigh in neighs:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)

            return size
        
        max_size = 0

        for i in range(n):
            for j in range(m):

                if marked[i][j]:
                    continue
                
                if grid[i][j]:
                    count += 1
                    size = bfs(i, j, count)
                    print(size)
                    max_size = max(size, max_size)


        return max_size