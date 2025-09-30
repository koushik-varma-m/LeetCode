class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        queue=nums
        while(len(queue)>1):
            t=[]
            for i in range(len(queue)-1):
                t.append((queue[i]+queue[i+1])%10)
            queue=t
        return queue[0]