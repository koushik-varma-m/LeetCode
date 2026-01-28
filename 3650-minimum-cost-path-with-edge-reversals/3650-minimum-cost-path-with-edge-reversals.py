class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        cost=[[] for _ in range(n)]
        for u,v,w in edges:
            cost[u].append([v,w])
            cost[v].append([u,2*w])
        vis=[False for _ in range(n)]
        dist=[float(inf) for _ in range(n)]
        dist[0]=0
        pq=[(0,0)]
        while pq:
            dis,cur=heapq.heappop(pq)
            if cur==n-1:
                return dis
            if vis[cur]:
                continue
            vis[cur]=True
            for v,w in cost[cur]:
                new_dist=dis+w
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    heapq.heappush(pq,(new_dist,v))
        return -1
            