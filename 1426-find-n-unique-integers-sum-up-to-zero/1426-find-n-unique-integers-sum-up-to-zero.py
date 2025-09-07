class Solution:
    def sumZero(self, n: int) -> List[int]:
        f=False
        if n%2==0:
            f=True
        ans=[]
        for i in range((n//2)*-1,(n//2)+1):
            if i==0 and f:
                continue
            ans.append(i)
        return ans