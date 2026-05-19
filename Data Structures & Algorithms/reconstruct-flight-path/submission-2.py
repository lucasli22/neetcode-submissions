class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        import heapq

        adj = defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)
        for f in adj:
            adj[f].sort()
    
        ans = []
    
        def rec(node):
            while adj[node]:
                to = adj[node].pop(0)
                rec(to)
            ans.append(node)
            return
        rec("JFK")
        return ans[::-1] 