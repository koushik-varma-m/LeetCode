class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans=float(-inf)
        for i in range(len(energy)-k):
            if energy[i]>0:
                energy[i+k]+=energy[i]
        for i in range(len(energy)-k,len(energy)):
            if energy[i]>ans:
                ans=energy[i]
        return ans