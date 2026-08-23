class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        maxes = {(i, j): float("infinity") for i in range(n) for j in range(n)}
        source = (0, 0)
        maxes[source] =  grid[0][0]
        heap = [(grid[0][0], source)]

        while heap:
            maxim, node = heapq.heappop(heap)
            i, j = node


            if maxim > maxes[node]:
                continue

            if node == (n-1, n-1):
                return maxim

            for d_i, d_j in DIRS:
                n_i, n_j = i + d_i, j + d_j
                if n_i >= 0 and n_i < n and n_j >= 0 and n_j < n:
                    new_max = max(maxim, grid[n_i][n_j])
                    if new_max < maxes[(n_i, n_j)]:
                        maxes[(n_i, n_j)] = new_max
                        heapq.heappush(heap, (new_max, (n_i, n_j)))

        return -1




