class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(m):
            d=defaultdict(int)
            for i in str(m):
                d[i]+=1
            for i in d:
                if int(i)!=d[i]:
                    return False
            return True
        for i in range(n+1,1224445):
            if check(i):   
                return i  