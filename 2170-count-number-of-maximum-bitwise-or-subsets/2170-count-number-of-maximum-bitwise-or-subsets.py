class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ansDic=defaultdict(int)
        def dfs(i,s):
            if i==len(nums):
                ansDic[s]+=1
                return 
            dfs(i+1,s)
            dfs(i+1,s|nums[i])
            return
        dfs(0,0)
        ans=0
        c=0
        for i in ansDic:
            if ansDic[i]>c:
                ans=i
                c=ansDic[i]
        return c