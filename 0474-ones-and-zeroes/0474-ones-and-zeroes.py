class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        temp=[]
        for s in strs:
            t=[0,0]
            for i in s:
                if i=="0":
                    t[0]+=1
                else:
                    t[1]+=1
            temp.append(t)
        dp={}
        def rec(idx,x,y):
            if idx==len(strs):
                return 0
            if (idx,x,y) in dp:
                return dp[(idx,x,y)]
            not_take=rec(idx+1,x,y)
            take=0
            if  x+temp[idx][0]<=m and y+temp[idx][1]<=n:
                take=1+rec(idx+1,x+temp[idx][0], y+temp[idx][1])
            dp[(idx,x,y)]=max(not_take,take)
            return dp[(idx,x,y)]
        return rec(0,0,0)
        