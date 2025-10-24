class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        l=len(str(n))
        if n==0:
            return 1
        if n<22:
            return 22
        if l<=6:
            ma=int("1"+l*str(l))
        else:
            ma=1224444
        def check(m):
            d=defaultdict(int)
            for i in str(m):
                d[i]+=1
            for i in d:
                if int(i)!=d[i]:
                    return False
            return True
        print(ma)
        for i in range(n+1,ma+1):
            if check(i):   
                return i  