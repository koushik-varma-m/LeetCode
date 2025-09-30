class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        flag=False
        while(x>=1 and y>=4):
            x-=1
            y-=4
            flag= not flag
        if flag:
            return "Alice"
        return "Bob"