class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid=set(["electronics","grocery","pharmacy","restaurant"])
        ans=[]
        def check_code(s):
            if not s:
                return False
            for i in s:
                if not("a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9" or i=="_"):
                    return False
            return True
        for idx,val in enumerate(businessLine):
            if val in valid:
                if check_code(code[idx]) and isActive[idx]:
                    ans.append([val,code[idx]])
        ans.sort()
        res=[]
        for x,y in ans:
            res.append(y)
        return res