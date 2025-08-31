class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        blocks=[[set() for i in range(3)] for _ in range(3)]
        def add(i,j,num):
            rows[i].add(num)
            cols[j].add(num)
            blocks[i//3][j//3].add(num)
        def remove(i,j,num):
            rows[i].remove(num)
            cols[j].remove(num)
            blocks[i//3][j//3].remove(num)
        back=[]
        val=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    back.append((i,j))
                    val.append(-1)
                    continue
                add(i,j,board[i][j])
        def check(i,j,num):
            if num in rows[i] or num in cols[j] or num in blocks[i//3][j//3]:
                return False
            return True
        def rec(idx):
            if idx==len(back):
                return True
            x,y=back[idx]
            for num in range(1,10):
                if check(x,y,str(num)):
                    add(x,y,str(num))
                    if rec(idx+1):
                        val[idx]=str(num)
                        return True
                    remove(x,y,str(num))
            return False
        rec(0)
        for i in range(len(back)):
            board[back[i][0]][back[i][1]]=val[i]