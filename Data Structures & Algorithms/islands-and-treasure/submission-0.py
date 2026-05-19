class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            i, j, dist = q.popleft()
            
            
            for idx in range(4):
                x = i + directions[idx][0]
                y = j + directions[idx][1]

                if x < 0 or x >= len(grid):
                    continue
                if y < 0 or y >= len(grid[0]):
                    continue
                if grid[x][y] == -1:
                    continue
                if grid[x][y] == INF:
                    grid[x][y] = dist + 1
                    q.append((x, y, dist + 1))
        
        return