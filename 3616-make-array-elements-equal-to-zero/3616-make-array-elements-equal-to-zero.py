class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def do(cur, dir, arr):
            while(0<=cur<len(nums)):
                if arr[cur]==0:
                    cur+=dir
                elif arr[cur]>0:
                    arr[cur]-=1
                    if dir==1:
                        dir=-1
                    else:
                        dir=1
                    cur+=dir
            for i in arr:
                if i!=0:
                    return False
            return True
        ans=0
        for i in range(len(nums)):
            if nums[i]!=0:
                continue
            if do(i,-1,nums.copy()):
                ans+=1
            if do(i,1,nums.copy()):
                ans+=1
        return ans