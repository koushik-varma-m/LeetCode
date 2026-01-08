class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp=dict()
        def rec(i,j):
            if i==len(nums1) or j==len(nums2):
                return float("-inf")
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=max(rec(i+1,j),nums1[i]*nums2[j],rec(i,j+1),rec(i+1,j+1)+nums1[i]*nums2[j])
            return dp[(i,j)]
        return rec(0,0)
