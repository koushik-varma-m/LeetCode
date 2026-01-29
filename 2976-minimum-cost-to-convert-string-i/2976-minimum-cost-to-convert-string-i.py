class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=[[] for _ in range(26)]
        for x,y,z in zip(original, changed, cost):
            adj[ord(x)-97].append((ord(y)-97,z))
        min_costs=[]
        for i in range(26):
            min_costs.append(self.dfs(i,adj))
        ans=0
        for s,t in zip(source,target):
            if s!=t:
                cur=min_costs[ord(s)-97][ord(t)-97]
                if cur==float('inf'):
                    return -1
                ans+=cur
        return ans
    def dfs(self,cur:int, adj:List[List[tuple]]) -> List[int]:
        pq=[(0, cur)]
        closest=[float("inf") for i in range(26)]
        while pq:
            cur_cost, cur_char = heapq.heappop(pq)
            if closest[cur_char]!=float("inf"):
                continue
            closest[cur_char]=cur_cost
            for tar_char, con_cost in adj[cur_char]:
                new_cost=cur_cost+con_cost
                if closest[tar_char]==float("inf"):
                    heapq.heappush(pq, (new_cost,tar_char))
        return closest