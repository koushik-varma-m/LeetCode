class Solution:
    def numSub(self, s: str) -> int:
        ans=0
        idx=0
        while(idx<len(s)):
            c=0
            while(idx<len(s) and s[idx]=="1"):
                idx+=1
                c+=1
            ans+=c*(c+1)//2
            if idx<len(s) and s[idx]=="0":
                idx+=1
        return ans%(10**9+7)