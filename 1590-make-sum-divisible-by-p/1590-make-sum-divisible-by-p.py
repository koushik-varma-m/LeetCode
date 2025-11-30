class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum=[0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1]+i)
        tot=sum(nums)%p
        if tot==0:
            return 0
        d=defaultdict()
        ans=len(nums)
        for idx,pre in enumerate(prefix_sum):
            if (pre-tot)%p in d:
                ans=min(ans,idx-(d[(pre-tot)%p]))
            d[pre%p]=idx
        return ans if ans!=len(nums) else -1