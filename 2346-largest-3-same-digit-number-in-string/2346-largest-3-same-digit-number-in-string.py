class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        for i in range(1,len(num)-1):
            if num[i]==num[i-1] and num[i]==num[i+1] and num[i-1:i+2]>ans:
                ans=num[i-1:i+2]
        return ans