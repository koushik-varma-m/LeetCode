class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d=defaultdict(int)
        for i in range(k):
            d[nums[i]]+=1
        ans=[]
        idx=0
        while(True):
            heap=[]
            for i in d:
                heapq.heappush(heap,[d[i],i])
                if len(heap)>x:
                    heapq.heappop(heap)
            cur=0
            for u,v in heap:
                cur+=u*v
            ans.append(cur)
            if idx+k==len(nums):
                break
            d[nums[idx]]-=1
            d[nums[idx+k]]+=1
            idx+=1
        return ans