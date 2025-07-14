class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,c in flights:
            adj[u].append([v,c])
        d=dict()
        minH=[[0,src,0]]
        while minH:
            cur,node,step=heapq.heappop(minH)
            if node==dst:
                return cur
            if step>k:
                continue
            if (node,step) in d and d[(node,step)]<cur:
                continue
            d[(node,step)]=cur
            for nei in adj[node]:
                if (nei[0],step+1) not in d or ((nei[0],step+1) in d and d[(nei[0],step+1)]>cur+nei[1]):
                    d[(nei[0],step+1)]=cur+nei[1]
                    heapq.heappush(minH,(cur+nei[1],nei[0],step+1))
        return -1