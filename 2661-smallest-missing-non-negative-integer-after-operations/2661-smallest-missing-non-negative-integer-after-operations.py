class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d=defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]%value]+=1
        ans=0
        while(True):
            t=ans%value
            if d[t]>0:
                ans+=1
                d[t]-=1
            else:
                break
        return ans