class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d=defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]%value]+=1
        ans=0
        while(d[ans%value]):
            d[ans%value]-=1
            ans+=1
        return ans