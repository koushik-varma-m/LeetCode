class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tot=sum(nums)
        cur=0
        ans=0
        for i in nums[:-1]:
            cur+=i
            if abs(cur-(tot-cur))%2==0:
                ans+=1
        return ans