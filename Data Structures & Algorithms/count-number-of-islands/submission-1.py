class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        n = len(grid)
        m = len(grid[0])

        marked = [[0 for j in range(m)] for i in range(n)]


        def neighbours(i, j):
            neighs = []
            if i>0 and grid[i-1][j] == "1":
                neighs.append((i-1, j))
            if i<n-1 and grid[i+1][j] == "1":
                neighs.append((i+1, j))
            if j>0 and grid[i][j-1] == "1":
                neighs.append((i, j-1))
            if j<m-1 and grid[i][j+1] == "1":
                neighs.append((i, j+1))

            return neighs

        def bfs(i, j, count):
            queue = deque()
            queue.append((i, j))
            visited = set()
            visited.add((i, j))
            
            while queue:
                i, j = queue.pop()
                marked[i][j] = count
                neighs = neighbours(i, j)
                for neigh in neighs:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
        

        for i in range(n):
            for j in range(m):

                if marked[i][j]:
                    continue
                
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j, count)

                    print(marked)

        return count
        