class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()

        ans = 0 
        def dfs(node: int):
            if node in visited:
                return 
            visited.add(node)
            for i in adjList[node]:
                dfs(i)
            
        for node in range(n):
            if node in visited:
                continue 
            dfs(node)
            ans += 1
        return ans