class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gap=[]
        prev=0
        for i in range(len(startTime)):
            gap.append(startTime[i]-prev)
            prev=endTime[i]
        gap.append(eventTime-prev)
        cur=0
        for i in range(k+1):
            cur+=gap[i]
        l=0
        ans=cur
        for r in range(k+1,len(gap)):
            cur-=gap[l]
            cur+=gap[r]
            if ans<cur:
                ans=cur
            l+=1
        return ans