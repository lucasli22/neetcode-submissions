class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m = len(board)
        n = len(board[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(x: int, y: int):
            visited.add((x, y))
            for idx in range(4):
                i = x + direction[idx][0]
                j = y + direction[idx][1]

                if i < 0 or i >= m:
                    continue
                if j < 0 or j >= n:
                    continue
                if (i, j) in visited:
                    continue
                if board[i][j] == "O":
                    dfs(i, j)
                
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m-1][i] == "O":
                dfs(m-1, i)
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if (i, j) not in visited:
                        board[i][j] = "X"
        