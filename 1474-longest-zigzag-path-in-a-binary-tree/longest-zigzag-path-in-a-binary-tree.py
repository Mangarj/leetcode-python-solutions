# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path=0
        def dfs(node):

            if not node:
                return (-1,-1)
            left=dfs(node.left)
            right=dfs(node.right)

            left_len=left[1]+1
            right_len=right[0]+1

            self.path=max(self.path,left_len,right_len)
            return(left_len,right_len)
        dfs(root)
        return self.path
        