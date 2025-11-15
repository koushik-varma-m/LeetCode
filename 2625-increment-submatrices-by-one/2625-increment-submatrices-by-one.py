class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        cur=0
        for x1,y1,x2,y2 in queries:
            for i in range(x1,x2+1):
                matrix[i][y1]+=1
                if y2+1==n:
                    continue
                matrix[i][y2+1]-=1
        for i in range(n):
            prev=0
            for j in range(n):
                matrix[i][j]+=prev
                prev=matrix[i][j]
        return matrix
