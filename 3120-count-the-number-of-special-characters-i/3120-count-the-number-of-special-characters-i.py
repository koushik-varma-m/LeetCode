class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=[0]*26
        C=[0]*26
        ans=0
        for c in word:
            print(ord(c))
            if ord(c)<97:
                C[ord(c)-65]+=1
            else:
                s[ord(c)-97]+=1
        for i in range(26):
            ans+=1 if min(s[i],C[i])>0 else 0
        return ans