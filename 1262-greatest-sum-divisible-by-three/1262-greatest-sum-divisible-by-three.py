class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ones=[]
        twos=[]
        tot=sum(nums)
        for i in nums:
            if i%3==1:
                heapq.heappush(ones,i*-1)
                if len(ones)==3:
                    heapq.heappop(ones)
            elif i%3==2:
                heapq.heappush(twos,i*-1)
                if len(twos)==3:
                    heapq.heappop(twos)
        if tot%3==1:
            cur=0
            if len(twos)==2:
                cur=tot+twos[0]+twos[1]
            if len(ones)==2:
                cur=max(tot+ones[1],cur)
            elif len(ones)==1:
                cur=max(tot+ones[0],cur)
            return cur
            
        elif tot%3==2:
            cur=0
            if len(ones)==2:
                cur=tot+ones[0]+ones[1]
            if len(twos)==2:
                cur=max(tot+twos[1],cur)
            elif len(twos)==1:
                cur=max(tot+twos[0],cur)
            return cur
        return tot
        