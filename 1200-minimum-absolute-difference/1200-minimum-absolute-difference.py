class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        mi=arr[-1]-arr[0]
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1]<mi:
                ans=[[arr[i-1],arr[i]]]
                mi=arr[i]-arr[i-1]
            elif arr[i]-arr[i-1]==mi:
                ans.append([arr[i-1],arr[i]])
        return ans