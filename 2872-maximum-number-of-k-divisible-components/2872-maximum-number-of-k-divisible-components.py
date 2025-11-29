class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.c=0
        def rec(node, vis):
            if node in vis:
                return 0
            vis.add(node)
            s=values[node]
            for n in adj[node]:
                if n not in vis:
                    s+=rec(n, vis)
            vis.remove(node)
            if s%k==0:
                self.c+=1
                return 0
            return s
        rec(0,set())
        return self.c