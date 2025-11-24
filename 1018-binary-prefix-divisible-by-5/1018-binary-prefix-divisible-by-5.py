class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur=0
        ans=[]
        for i in nums:
            cur=cur<<1
            cur+=i
            ans.append(cur%5==0)
        return ans