class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di=dict()
        for i,n in enumerate(nums):
            if target-n in di:
                return [di[target-n],i]
            di[n]=i
        return [-1,-1]