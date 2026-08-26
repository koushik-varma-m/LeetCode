class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if k==1 and "1" in s:
            return "1"
        ans=s+"1"
        for i in range(len(s)-1):
            if s[i]=="1":
                c=1
                for j in range(i+1, len(s)):
                    if s[j]=="1":
                        c+=1
                    if c==k:
                        ans=s[i:j+1] if int(ans)>int(s[i:j+1]) else ans
        return ans if ans!=s+"1" else ""