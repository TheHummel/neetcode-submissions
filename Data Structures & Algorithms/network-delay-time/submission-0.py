class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}

        for edge in times:
            u, v, time = edge
            if u not in edges:
                edges[u] = [(v, time)]
            else:
                edges[u].append((v, time))

        dist = {node: float('inf') for node in range(1, n+1)}

        dist[k] = 0

        heap = [(0, k)]
        heapq.heapify(heap)
        print(heap)
        visited = set()

        while heap:
            _, u = heapq.heappop(heap)
            visited.add(u)

            print("checking node", u)
            if u not in edges:
                continue

            for out in edges[u]:
                v, t = out

                print("out,", v, t)

                if v not in visited:
                    dist[v] = min(dist[v], dist[u] + t)

                    heapq.heappush(heap, (dist[v], v))

            
        max_val = max(dist.values())

        return max_val if max_val != float('inf') else -1

        

