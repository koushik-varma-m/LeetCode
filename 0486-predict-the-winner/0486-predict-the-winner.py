class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache
        def rec(i,j):
            if i==j:
                return nums[i]
            p_l=nums[i]-rec(i+1,j)
            p_r=nums[j]-rec(i,j-1)
            return max(p_l,p_r)
        return rec(0,len(nums)-1)>=0