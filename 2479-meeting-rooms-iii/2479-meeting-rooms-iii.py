class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free=[]
        for i in range(n):
            heapq.heappush(free,i)
        print(free)
        oc=[]
        d=defaultdict(int)
        cur=0
        for s,e in meetings:
            cur=max(s,cur)
            while oc and cur>=oc[0][0]:
                    t,r=heapq.heappop(oc)
                    heapq.heappush(free,r)
            if not free:
                cur,r=heapq.heappop(oc)
                heapq.heappush(free,r)
                while oc and cur==oc[0][0]:
                    t,r=heapq.heappop(oc)
                    heapq.heappush(free,r)
            r=heapq.heappop(free)
            heapq.heappush(oc,[e+cur-s,r])
            d[r]+=1
        ansRoom=0
        cur=d[0]
        for i in range(1,n):
            if d[i]>cur:
                ansRoom=i
                cur=d[i]
        return ansRoom