class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            r=""
            for i in range(len(s)-1):
                r+=str((int(s[i])+int(s[i+1]))%10)
            s=r
        return s[0]==s[1]