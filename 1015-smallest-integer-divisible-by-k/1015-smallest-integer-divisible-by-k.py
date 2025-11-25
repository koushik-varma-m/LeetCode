class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        x=""
        c=0
        while(True):
            c+=1
            x+="1"
            rem = int(x)%k
            if rem==0:
                return c
            x=str(rem)
        

