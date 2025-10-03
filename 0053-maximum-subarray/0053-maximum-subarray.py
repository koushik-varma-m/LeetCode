class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        ans=nums[0]
        for i in range(len(nums)):
            cur+=nums[i]
            ans=max(cur,ans)
            if cur<0:
                cur=0
        return ans