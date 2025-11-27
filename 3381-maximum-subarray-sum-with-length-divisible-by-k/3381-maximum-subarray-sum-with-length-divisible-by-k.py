class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=[0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        ans=float(-inf)
        cum_sum=prefix_sum.copy()
        for i in range(len(prefix_sum)):
            temp=0
            if i-k>=0:
                temp=prefix_sum[i]-prefix_sum[i-k]
                temp=max(cum_sum[i-k]+temp, temp)
            cum_sum[i]=temp
        for i in range(k,len(cum_sum)):
            ans=max(ans,cum_sum[i])
        return ans