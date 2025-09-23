class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=[int(i) for i in version1.split(".")]
        v2=[int(j) for j in version2.split(".")]
        n=min(len(v1),len(v2))
        for i in range(n):
            if v1[i]<v2[i]:
                return -1
            elif v1[i]>v2[i]:
                return 1
        if len(v1)==len(v2):
            return 0
        while(n<len(v1)):
            if v1[n]!=0:
                return 1
            n+=1
        while(n<len(v2)):
            if v2[n]!=0:
                return -1
            n+=1
        return 0