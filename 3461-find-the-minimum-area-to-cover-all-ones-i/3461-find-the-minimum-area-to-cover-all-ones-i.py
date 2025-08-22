class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top=len(grid)
        bot=-1
        left=len(grid[0])
        right=-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    top=min(top,i)
                    bot=max(bot,i)
                    left=min(left,j)
                    right=max(right,j)
        return (bot-top+1)*(right-left+1)
