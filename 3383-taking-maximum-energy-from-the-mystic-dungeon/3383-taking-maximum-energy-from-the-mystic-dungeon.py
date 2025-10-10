class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans=float(-inf)
        for i in range(len(energy)):
            if i+k>=len(energy):
                ans=max(energy[i],ans)
                continue
            if energy[i]>0:
                energy[i+k]+=energy[i]
        return ans