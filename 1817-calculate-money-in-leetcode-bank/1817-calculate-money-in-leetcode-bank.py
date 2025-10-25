class Solution:
    def totalMoney(self, n: int) -> int:
        f=n//7
        rem=n%7
        ans=0
        for i in range(f):
            ans+=(((7+i)*(8+i)//2)-(i*(i+1)//2))
        ans+=(((f+rem)*(f+rem+1)//2)-(f*(f+1)//2))
        return ans