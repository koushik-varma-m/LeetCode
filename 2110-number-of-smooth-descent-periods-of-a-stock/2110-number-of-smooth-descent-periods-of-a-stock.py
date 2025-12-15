class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev=prices[0]
        cur=1
        ans=0
        for i in prices[1:]:
            if i==prev-1:
                cur+=1
            else:
                ans+=(cur*(cur+1)//2)
                cur=1
            prev=i
        ans+=(cur*(cur+1)//2)
        return ans