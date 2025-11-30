class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d=dict()
        ans=len(nums)
        for i,v in enumerate(nums):
            k=int(str(v)[::-1])
            if v in d:
                ans=min(ans,i-d[v])
            d[k]=i
        return ans if ans!=len(nums) else -1