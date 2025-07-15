class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowels={'a','e','i','o','u'}
        v,c=False,False
        for i in word:
            if "0"<=i<="9":
                continue
            elif "a"<=i<="z" or "A"<=i<="Z":
                if v and c:
                    continue
                if i.lower() in vowels:
                    v=True
                else:
                    c=True
            else:
                return False
        return v and c