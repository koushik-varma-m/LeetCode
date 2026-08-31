# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        cur=head.next
        critical_points=[]
        idx=2
        while(cur):
            if not cur.next:
                break
            if (cur.val>prev.val and cur.val>cur.next.val) or (cur.val<prev.val and cur.val<cur.next.val):
                critical_points.append(idx)
            prev=cur
            cur=cur.next
            idx+=1
        if len(critical_points)<2:
            return [-1,-1]
        print(critical_points)
        ans=[float("inf"),critical_points[-1]-critical_points[0]]
        for i in range(1,len(critical_points)):
            ans[0]=min(ans[0],critical_points[i]-critical_points[i-1])
        return ans