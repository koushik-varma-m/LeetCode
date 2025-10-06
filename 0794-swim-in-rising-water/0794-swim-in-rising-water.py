class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0],(0,0))]
        vis=set()
        vis.add((0,0))
        adj=[(0,-1),(0,1),(1,0),(-1,0)]
        while(minHeap):
            cur=heapq.heappop(minHeap)
            if cur[1][0]==len(grid)-1 and cur[1][1]==len(grid)-1:
                return cur[0]
            for d in adj:
                x1=cur[1][0]+d[0]
                y1=cur[1][1]+d[1]
                if x1>=0 and x1<len(grid) and y1>=0 and y1<len(grid) and (x1,y1) not in vis:
                    heapq.heappush(minHeap,(max(cur[0],grid[x1][y1]),(x1,y1)))
                    vis.add((x1,y1))
        return -1