class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        res = math.log10(n) / math.log10(4)
        return abs(res - round(res)) < 1e-10