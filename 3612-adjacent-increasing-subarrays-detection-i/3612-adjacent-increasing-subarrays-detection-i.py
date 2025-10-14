class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev=nums[0]
        cur=1
        prevC=1
        for i in range(1,len(nums)):
            if (prevC>=k and cur>=k) or cur>=2*k:
                    return True
            if nums[i]>prev:
                cur+=1
                prev=nums[i]
            else:
                prev=nums[i]
                prevC=cur
                cur=1
        if (prevC>=k and cur>=k) or cur>=2*k:
            return True
        return False