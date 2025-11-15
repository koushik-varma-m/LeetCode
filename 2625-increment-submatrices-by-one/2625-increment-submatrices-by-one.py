class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        cur=0
        while(cur<n):
            cols=[0 for _ in range(n+1)]
            for x1,y1,x2,y2 in queries:
                if x1<=cur<=x2:
                    cols[y1]+=1
                    cols[y2+1]-=1
            prev=0
            for i in range(n):
                cols[i]+=prev
                prev=cols[i]
            for i in range(n):
                matrix[cur][i]=cols[i]
            cur+=1
        return matrix

        #     for i in range(x1,x2+1):
        #         for j in range(y1,y2+1):
        #             matrix[i][j]+=1
        return matrix
