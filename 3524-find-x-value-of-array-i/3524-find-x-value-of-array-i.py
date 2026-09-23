class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans=[0 for _ in range(k)]
        dp=[0 for _ in range(k)]
        for n in nums:
            nex=[0 for _ in range(k)]
            cur=n%k
            nex[cur]+=1
            for r in range(k):
                newR = (cur*r)%k
                nex[newR]+=dp[r]
            for r in range(k):
                ans[r]+=nex[r]
            dp=nex
        return ans