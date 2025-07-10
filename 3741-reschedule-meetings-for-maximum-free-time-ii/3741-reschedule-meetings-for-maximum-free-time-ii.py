class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n=len(startTime)
        pos=[False for _ in range(n)]
        gap=[0 for _ in range(n)]
        prevL=0
        prevR=eventTime
        leftM=0
        rightM=0
        ans=0
        for i in range(n):
            if leftM>=(endTime[i]-startTime[i]):
                pos[i]= True
            gap[i]+=startTime[i]-prevL
            leftM=max(leftM, startTime[i]-prevL)
            prevL=endTime[i]
            if rightM>=(endTime[n-1-i]-startTime[n-1-i]):
                pos[n-1-i]=True
            gap[n-1-i]+=prevR-endTime[n-1-i]
            rightM=max(rightM, prevR-endTime[n-1-i])
            prevR=startTime[n-1-i]
        ans=0
        for i in range(n):
            if pos[i]:
                ans=max(ans, gap[i]+endTime[i]-startTime[i])
            else:
                ans=max(ans,gap[i])
        return ans