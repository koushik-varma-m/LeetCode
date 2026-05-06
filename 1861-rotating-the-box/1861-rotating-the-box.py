class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rotated_box=[]
        m=len(boxGrid)
        n=len(boxGrid[0])
        for i in range(0, n):
            temp=[]
            for j in range(m-1,-1,-1):
                temp.append(boxGrid[j][i])
            rotated_box.append(temp)
        print(rotated_box)
        for i in range(0,m):
            for j in range(n-2,-1,-1):
                if rotated_box[j][i]=="#":
                    cur=j
                    while cur+1<n and rotated_box[cur+1][i]==".":
                        rotated_box[cur+1][i]="#"
                        rotated_box[cur][i]="."
                        cur+=1
        return rotated_box
        pass
