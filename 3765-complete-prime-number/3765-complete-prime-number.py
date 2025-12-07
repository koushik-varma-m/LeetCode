class Solution:
    def completePrime(self, num: int) -> bool:
        def checkPrime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        f=""
        r=""
        for i in range(len(str(num))):
            f+=str(num)[i]
            r=str(num)[len(str(num))-1-i]+r
            if checkPrime(int(f)) and checkPrime(int(r)):
                continue
            return False
        return True
