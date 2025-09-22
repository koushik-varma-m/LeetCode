class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        ans=0
        c=0
        for i in d:
            if d[i]>c:
                c=d[i]
                ans=c
            elif d[i]==c:
                ans+=c
            else:
                continue
        return ans