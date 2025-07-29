class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in s:
            if i+1 not in s:
                t=1
                while i-t in s:
                    t+=1
                ans=max(ans,t)
        return ans