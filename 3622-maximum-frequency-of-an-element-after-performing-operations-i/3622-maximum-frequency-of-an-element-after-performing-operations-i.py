class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        c=Counter(nums)
        keys=list(c.keys())
        keys.sort()
        count=[0]
        cur=0
        for i in range(len(keys)):
            cur+=c[keys[i]]
            count.append(cur)
        l=0
        h=-1
        ans=0
        print(count)
        for i in range(keys[0],keys[-1]+1):
            while(l<len(keys) and i-k>keys[l]):
                l+=1
            while(h+1<len(keys) and i+k>=keys[h+1]):
                h+=1
            temp=count[h+1]-count[l]
            temp-=c[i]
            if temp>numOperations:
                ans=max(numOperations+c[i],ans)
            else:
                ans=max(temp+c[i],ans)
        return ans

