class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        ans = 0

        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            parent[pa] = pb
            return True

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()

        count = 0
        while count < n - 1:
            dist, i, j = edges.pop(0)
            if union(i, j):
                count += 1
                ans += dist

        return ans