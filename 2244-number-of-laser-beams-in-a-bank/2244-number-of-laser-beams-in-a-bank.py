class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        c=0
        for i in bank:
            v = i.count("1")
            if v!=0:
                c+= v*prev
                prev=v
        return c
