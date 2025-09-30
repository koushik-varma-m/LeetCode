class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d=dict()
        for i in range(n):
            d[i]=defaultdict(int)
        for x,y in pick:
            d[x][y]+=1
        ans=0
        for i in d:
            for j in d[i]:
                if d[i][j]>i:
                    ans+=1
                    break
        return ans