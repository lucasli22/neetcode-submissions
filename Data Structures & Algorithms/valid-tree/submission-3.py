class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        path = set()
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            if u == v:
                return False
            adjList[u].append(v)
            adjList[v].append(u)
        def hasCycle(node: int, prev: int) -> bool:
            visited.add(node)

            for i in adjList[node]:
                if i == prev:
                    continue
                if i in visited:
                    return True
                if hasCycle(i, node):
                    return True

            return False
        if hasCycle(0, -1):
            return False
        if len(visited) < n:
            return False
        return True
        