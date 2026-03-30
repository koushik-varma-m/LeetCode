class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        eve=[0 for i in range(26)]
        odd=[0 for i in range(26)]
        for i in range(len(s1)):
            if i%2==0:
                eve[ord(s1[i])-97]+=1
                eve[ord(s2[i])-97]-=1
            else:
                odd[ord(s1[i])-97]+=1
                odd[ord(s2[i])-97]-=1
        for i in range(26):
            if eve[i]!=0 or odd[i]!=0:
                return False
        return True