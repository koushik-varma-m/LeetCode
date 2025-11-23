class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans+=min(3-(i%3),i%3)
        return ans