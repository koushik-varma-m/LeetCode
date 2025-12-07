class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def generate(n):
            s=""
            while(n):
                s=str(n%2)+s
                n//=2
            return s
        def checkP(n):
            s=generate(n)
            return s==s[::-1]
        def check(n):
            for i in range(n):
                if checkP(n-i) or checkP(n+i):
                    return i
        ans=[]
        for i in nums:
            ans.append(check(i))
        return ans