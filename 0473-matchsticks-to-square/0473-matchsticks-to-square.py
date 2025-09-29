class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot=sum(matchsticks)
        each=tot//4
        if each*4 != tot:
            return False
        matchsticks.sort(reverse=True)
        def rec(idx,a,b,c,d):
            if idx==len(matchsticks):
                return True
            if a>each or b>each or c>each or d>each:
                return False
            ans=False
            if a+matchsticks[idx]<=each:
                ans= ans or rec(idx+1,a+matchsticks[idx],b,c,d)
            if b+matchsticks[idx]<=each:
                ans= ans or rec(idx+1,a,b+matchsticks[idx],c,d)
            if c+matchsticks[idx]<=each:
                ans= ans or rec(idx+1,a,b,c+matchsticks[idx],d)
            if d+matchsticks[idx]<=each:
                ans= ans or rec(idx+1,a,b,c,d+matchsticks[idx])
            return ans

        return rec(0,0,0,0,0)