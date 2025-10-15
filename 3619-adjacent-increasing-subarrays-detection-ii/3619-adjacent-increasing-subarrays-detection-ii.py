class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        a=0
        cur=1
        prev=nums[0]
        ans=1
        for i in range(1,len(nums)):
            if nums[i]>prev:
                cur+=1
                prev=nums[i]
            else:
                ans=max(min(a,cur),ans)
                ans=max(ans,cur//2)
                a=cur
                cur=1
                prev=nums[i]
        ans=max(min(a,cur),ans)
        ans=max(ans,cur//2)
        return ans