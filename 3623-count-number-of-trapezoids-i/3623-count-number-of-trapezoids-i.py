class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d=defaultdict(int)
        for x,y in points:
            d[y]+=1
        ans=0
        tot_possible=0
        for i in d:
            if d[i]>=2:
                possible=(d[i]*(d[i]-1)//2)
                ans+=(tot_possible*possible)
                tot_possible+=possible
        return ans%(10**9+7)