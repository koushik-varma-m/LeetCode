class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[defaultdict(int) for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]%k]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if j>0:
                    for rem,c in dp[i][j-1].items():
                        dp[i][j][(rem+grid[i][j])%k]+=c
                if i>0:
                    for rem,c in dp[i-1][j].items():
                        dp[i][j][(rem+grid[i][j])%k]+=c
                        dp[i][j][(rem+grid[i][j])%k]=dp[i][j][(rem+grid[i][j])%k]%(10**9+7)
        return dp[-1][-1][0]