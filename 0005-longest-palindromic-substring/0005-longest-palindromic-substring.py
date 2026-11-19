class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        res=s[0]
        for i in range(len(s)-1):
            p1=check(i,i+1)
            if len(p1)>len(res):
                res=p1
            p2=check(i,i)
            if len(p2)>len(res):
                res=p2
        return res