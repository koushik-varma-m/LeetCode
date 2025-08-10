class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        while(n>0):
            c+=n%2
            n//=2
        return c==1
        