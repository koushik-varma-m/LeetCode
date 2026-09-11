# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0
        def rec(node):
            if not node:
                return [0,0]
            left=rec(node.left)
            right=rec(node.right)
            c=left[0]+right[0]+1
            v=left[1]+right[1]+node.val
            if node.val==(v//c):
                self.ans+=1
            return [c,v]
        rec(root)
        return self.ans
