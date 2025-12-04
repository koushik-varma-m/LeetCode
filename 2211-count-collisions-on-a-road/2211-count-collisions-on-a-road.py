class Solution:
    def countCollisions(self, directions: str) -> int:
        c=-1
        ans=0
        for i in directions:
            if i=="L":
                if c==0:
                    ans+=1
                elif c>0:
                    ans+=1+c
                    c=0
            elif i=="S":
                if c>0:
                    ans+=c
                c=0
            else:
                if c==-1:
                    c=1
                else:
                    c+=1
            print(ans,c)
        return ans