# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def tot(node):
            if not node:
                return 0
            return node.val+tot(node.left)+tot(node.right)
        self.total=tot(root)
        self.ans=0
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.ans=max(self.ans,(self.total-right)*right,(self.total-left)*left)
            return node.val+left+right
        dfs(root)
        return self.ans%(10**9+7)