class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        st=set()
        def rec(s):
            if s in st:
                return
            st.add(s)
            rec(s[-b:]+s[:-b])
            for i in range(1,len(s),2):
                t=(int(s[i])+a)%10
                s=s[:i]+str(t)+s[i+1:]
            rec(s)
            return 
        rec(s)
        return min(st)
