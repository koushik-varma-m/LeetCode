class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                k=int(sqrt(i**2+j**2+1))
                if k<=n and k**2==i**2+j**2:
                    ans+=1
        return ans