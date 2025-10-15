class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        a=[]
        cur=1
        prev=nums[0]
        ans=1
        for i in range(1,len(nums)):
            if nums[i]>prev:
                cur+=1
                prev=nums[i]
            else:
                if len(a):
                    ans=max(min(a[-1],cur),ans)
                ans=max(ans,cur//2)
                a.append(cur)
                cur=1
                prev=nums[i]
        if len(a):
            ans=max(min(a[-1],cur),ans)
        ans=max(ans,cur//2)
        return ans