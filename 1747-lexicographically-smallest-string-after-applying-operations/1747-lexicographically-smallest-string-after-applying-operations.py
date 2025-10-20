class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        se = set()
        def rec(st):
            if st in se:
                return 
            se.add(st)
            
            rec(st[-b:]+st[:-b])

            x=""
            for i,v in enumerate(st):
                if i%2==0:
                    x+=v
                else:
                    t = int(v)+a
                    x+=str(t)[-1]
            rec(x)

        rec(s)
        return min(se)