class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=[[float("inf") for _ in range(26)] for _ in range(26)]
        for x,y,z in zip(original,changed,cost):
            adj[ord(x)-97][ord(y)-97]=min(adj[ord(x)-97][ord(y)-97],z)       
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])
        ans=0
        for i,j in zip(source,target):
            if i==j:
                continue
            if adj[ord(i)-97][ord(j)-97]==float("inf"):
                return -1
            ans+=adj[ord(i)-97][ord(j)-97]
        return ans