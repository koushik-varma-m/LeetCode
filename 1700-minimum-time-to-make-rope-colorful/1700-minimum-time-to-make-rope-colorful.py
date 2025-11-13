class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=0
        ans=0
        while(i<len(colors)):
            c=0
            ma=0
            t=0
            cur=colors[i]
            while(i<len(colors) and colors[i]==cur):
                c+=1
                t+=neededTime[i]
                ma=max(ma,neededTime[i])
                i+=1
            if c>1:
                t-=ma
                ans+=t
        return ans