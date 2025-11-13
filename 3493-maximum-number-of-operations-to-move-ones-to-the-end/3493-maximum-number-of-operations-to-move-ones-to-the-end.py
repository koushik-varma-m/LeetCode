class Solution:
    def maxOperations(self, s: str) -> int:
        i=0
        c=0
        ans=0
        while(i<len(s)):
            if s[i]=="1":
                c+=1
                i+=1
            else:
                while(i<len(s) and s[i]=="0"):
                    i+=1
                ans+=c
        return ans
