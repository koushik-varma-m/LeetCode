class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans=nums[0]
        mini=float("inf")
        nex_mini=float("inf")
        for i in nums[1:]:
            if i<=mini:
                nex_mini=mini
                mini=i
            elif i<=nex_mini:
                nex_mini=i
        return ans+mini+nex_mini
