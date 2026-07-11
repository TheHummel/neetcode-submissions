class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        n = len(grid)
        m = len(grid[0])

        if n<1 and m <1:
            return -1

        def neighbours(i, j):
            neighs = []
            if i > 0 and grid[i-1][j] == 1:
                neighs.append((i-1,j))
            if i < n-1 and grid[i+1][j] == 1:
                neighs.append((i+1,j))
            if j > 0 and grid[i][j-1] == 1:
                neighs.append((i,j-1))
            if j < m-1 and grid[i][j+1] == 1:
                neighs.append((i,j+1))

            return neighs

        days = 0
        fresh = 0

        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while fresh and queue:
            rotten = len(queue)

            for i in range(rotten):

                cell = queue.popleft()
                i, j = cell

                neighs = neighbours(i, j)

                for neigh in neighs:
                    r, c = neigh
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh -= 1

            days += 1


        return days if fresh == 0 else -1



        """def bfs(i, j):
            visited = set()
            queue = deque()

            days = 0

            queue.append(((i,j), 0))

            rotten.add((i,j))

            while queue:
                cell = queue.popleft()
                (i, j), day = cell
                visited.add((i, j))
                neighs = neighbours(i, j)

                days = max(day, days)

                for neigh in neighs:
                    rotten.add(neigh)
                    if neigh not in visited:
                        queue.append((neigh, day + 1))

            return days


        marked = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2 and not (i, j) in rotten:
                    max_days = max(bfs(i, j), max_days)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not (i, j) in rotten:
                    return -1

        return max_days"""
        