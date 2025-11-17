class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c=k
        for i in nums:
            if i==0:
                c+=1
            else:
                if c>=k:
                    c=0
                else:
                    return False
        return True