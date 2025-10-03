class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        nums[-1]=True
        for i in range(n-2, -1, -1):
            c=nums[i]
            nums[i]=False
            for j in range(i+1, i+c+1):
                if nums[j]:
                    nums[i]=True
                    break
        return nums[0]