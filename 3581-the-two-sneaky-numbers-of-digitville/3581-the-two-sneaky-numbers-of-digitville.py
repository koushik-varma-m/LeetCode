class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set()
        for i in nums:
            if i in s:
                ans.append(i)
            s.add(i)
        return ans