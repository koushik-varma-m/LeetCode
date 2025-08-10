class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_digits(n):
            count=[0 for _ in range(10)]
            if n==0:
                count[0]+=1
            while n>0:
                count[n%10]+=1
                n//=10
            return count
        given=get_digits(n)
        for i in range(30):
            cur=1<<i
            if get_digits(cur)==given:
                return True
        return False