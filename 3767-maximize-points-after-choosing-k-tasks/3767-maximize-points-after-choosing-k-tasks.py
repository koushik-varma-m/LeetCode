class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        ans=0
        n=len(technique1)
        vis=[False for i in range(n)]
        for i in range(n):
            if technique1[i]>=technique2[i]:
                ans+=technique1[i]
                vis[i]=True
                k-=1
        heap=[]
        if k>0:
            for i in range(n):
                if not vis[i]:
                    heapq.heappush(heap,(-1*(technique2[i]-technique1[i]),i))
                    if len(heap)>k:
                        heapq.heappop(heap)
            for i,j in heap:
                ans+=technique1[j]
                vis[j]=True
        for i in range(n):
            if not vis[i]:
                ans+=max(technique1[i],technique2[i])
        return ans