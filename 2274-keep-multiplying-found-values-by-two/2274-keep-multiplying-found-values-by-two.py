class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        cur=1
        nums=set(nums)
        while original*cur in nums:
            cur*=2
        return original*cur