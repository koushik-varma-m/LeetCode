class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp={}
        def dfs(r,c):
            if r==len(triangle):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            cur=triangle[r][c]
            if c+1<=r+1:
                cur+=min(dfs(r+1,c),dfs(r+1,c+1))
            else:
                cur+=dfs(r+1,c)
            dp[(r,c)]=cur
            return cur
        return dfs(0,0)