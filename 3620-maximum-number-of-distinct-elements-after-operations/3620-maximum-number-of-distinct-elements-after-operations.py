class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur=nums[0]-k
        ans=0
        for i in range(len(nums)):
            if cur>=nums[i]-k and cur<=nums[i]+k:
                ans+=1
                cur+=1
                continue
            if cur<nums[i]:
                cur=nums[i]-k
                ans+=1
                cur+=1
                continue
        return ans