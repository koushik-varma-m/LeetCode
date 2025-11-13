class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix=[[0 for i in range(n)] for _ in range(m)]
        for u,v in guards:
            matrix[u][v]="G"
        for u,v in walls:
            matrix[u][v]="W"
        for i in range(m):
            cur=0
            for j in range(n):
                if matrix[i][j]=="G":
                    cur=1
                elif matrix[i][j]=="W":
                    cur=0
                elif matrix[i][j]!=1:
                    matrix[i][j]=cur
        for i in range(m):
            cur=0
            for j in range(n-1,-1,-1):
                if matrix[i][j]=="G":
                    cur=1
                elif matrix[i][j]=="W":
                    cur=0
                elif matrix[i][j]!=1:
                    matrix[i][j]=cur
        for j in range(n):
            cur=0
            for i in range(m):
                if matrix[i][j]=="G":
                    cur=1
                elif matrix[i][j]=="W":
                    cur=0
                elif matrix[i][j]!=1:
                    matrix[i][j]=cur
        for j in range(n):
            cur=0
            for i in range(m-1,-1,-1):
                if matrix[i][j]=="G":
                    cur=1
                elif matrix[i][j]=="W":
                    cur=0
                elif matrix[i][j]!=1:
                    matrix[i][j]=cur
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    ans+=1
        return ans
