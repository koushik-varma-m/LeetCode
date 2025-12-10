class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mi=complexity[0]
        for i in complexity[1:]:
            if i<=mi:
                return 0
        ans=1
        for i in range(1,len(complexity)):
            ans=(ans*i)%(10**9+7)
        return ans%(10**9+7)