class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k==0:
            return len(nums)
        nums.sort()
        tot=len(nums)
        ans=0
        c=0
        for i,v in enumerate(nums):
            if i==0:
                c=1
                continue
            if v==nums[i-1]:
                c+=1
                continue
            if len(nums)-i<k:
                break
            ans=ans+c
            c=1
        return ans            