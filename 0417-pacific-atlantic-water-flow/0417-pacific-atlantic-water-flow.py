class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m=len(heights),len(heights[0])
        pac,alt=set(),set()
        def dfs(r,c,preH,s):
            if (r,c) in s or r<0 or c<0 or r>=n or c>=m or heights[r][c]<preH:
                return
            s.add((r,c))
            dfs(r-1,c,heights[r][c],s)
            dfs(r+1,c,heights[r][c],s)
            dfs(r,c-1,heights[r][c],s)
            dfs(r,c+1,heights[r][c],s)
        for i in range(m):
            dfs(0,i,heights[0][i],pac)
            dfs(n-1,i,heights[n-1][i],alt)
        for i in range(n):
            dfs(i,0,heights[i][0],pac)
            dfs(i,m-1,heights[i][m-1],alt)
        ans=[]
        for pair in pac:
            if pair in alt:
                ans.append(list(pair))
        return ans