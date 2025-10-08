class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def search(k):
            l=0
            r=len(potions)-1
            ans=r+1
            while(l<=r):
                mid=(l+r)//2
                if potions[mid]*k<success:
                    l=mid+1
                else:
                    ans=mid
                    r=mid-1
            return len(potions)-ans if ans!=len(potions) else 0
        ans=[]
        for i in range(len(spells)):
            ans.append(search(spells[i]))
        return ans