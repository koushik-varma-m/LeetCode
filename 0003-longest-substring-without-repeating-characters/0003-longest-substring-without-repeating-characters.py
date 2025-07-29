class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur=set()
        l=0
        ans=0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l+=1
            cur.add(s[r])
            ans=max(ans,r-l+1)
        return ans