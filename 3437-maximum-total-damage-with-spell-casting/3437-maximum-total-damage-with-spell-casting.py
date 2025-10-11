class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        dp=[]
        ans=0
        i=0
        while i<len(power):
            cur=power[i]
            k=0
            while(i<len(power) and power[i]==cur):
                k+=1
                i+=1
            t=cur*k
            j=len(dp)-1
            while(j>=0):
                if dp[j][0]+2<cur:
                    t+=(dp[j][1])
                    break
                j-=1
            ans=max(ans,t)
            dp.append((cur,ans))
        return ans