class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq

        adj = defaultdict(list)
        n = len(grid)

        dist = [[float("inf")] * n for _ in range(n)]
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))
        dist[0][0] = grid[0][0]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while pq:
            d, i, j = heapq.heappop(pq)
            
            if d > dist[i][j]: continue 

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if x >= n or x < 0: continue
                if y >= n or y < 0: continue 


                alt = max(d, grid[x][y])

                if alt < dist[x][y]:
                    dist[x][y] = alt
                    heapq.heappush(pq, (alt, x, y))
        print(dist)
        return dist[-1][-1]
        