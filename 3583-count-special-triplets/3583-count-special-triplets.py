class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        d=defaultdict(int)
        cur=[]
        ans=0
        for i in nums:
            cur.append(d[i*2])
            d[i]+=1
        d=defaultdict(int)
        for i,j in zip(nums[::-1],cur[::-1]):
            ans+=j*d[i*2]
            d[i]+=1
        return ans%(10**9+7)